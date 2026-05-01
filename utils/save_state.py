import utils.req_interface as r
import utils.user_data as user
import json
import app_state

APP_ID = user.get_app_id()
APP_IP = user.get_app_ip()

def save_state():

    # dash_row_values: for state tracking of UI row values
    if app_state.dash_row_values:
        json_values = json.dumps(app_state.dash_row_values, indent=4)
        print(json_values)  

        sync_state(json_values)


    # dash_rows: for tracking how many rows there are total
    if app_state.dash_rows >= 0:
        data = {
            "rows": app_state.dash_rows
        }
        json_values = json.dumps(data, indent=4)
        print(json_values)

        sync_state(json_values)




def sync_state(json_values):
    update_res = r.request.update(APP_ID, json_values)

    # general errors
    if isinstance(update_res, Exception):
        print(f"Network or connection error during update: {update_res}")

    # not found
    elif update_res.status_code == 404:
        print(f"App ID {APP_ID} not found. Attempting creation...")
        r.request.create(json_values)
        update_res = r.request.read(APP_ID)

    # other errors
    elif update_res.status_code not in (200, 204):
        print(f"Update failed with HTTP {update_res.status_code}: {update_res.text}")

    # Success
    else:
        print("Update successful.")

    