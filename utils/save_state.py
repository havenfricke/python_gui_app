import utils.req_interface as r
import utils.user_data as user
import app_state

APP_ID = user.get_app_id()
APP_IP = user.get_app_ip()

def save_state():
    # Construct a single payload matching the expected backend schema keys
    update_payload = {
        "app_id": APP_ID,
        "app_metadata": app_state.dash_row_values if app_state.dash_row_values else {},
        "app_rows": app_state.dash_rows if app_state.dash_rows >= 0 else 0
    }
    
    print(f"Dispatching update payload: {update_payload}")
    
    # Pass the raw Python dictionary; r.request.update will handle serialization
    sync_state(update_payload)

def sync_state(payload):
    update_res = r.request.update(APP_ID, payload)

    # general errors
    if isinstance(update_res, Exception):
        print(f"Network or connection error during update: {update_res}")

    # not found
    elif update_res.status_code == 404:
        print(f"App ID {APP_ID} not found.")

    # other errors
    elif update_res.status_code not in (200, 204):
        if update_res.text[0] == "0":
            print(update_res.text)
        else:
            print(f"Update failed with HTTP {update_res.status_code}: {update_res.text}")

    # Success
    else:
        print("Update successful.")