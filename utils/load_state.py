import json
import app_state
import utils.req_interface as r
import utils.user_data as user

APP_ID = user.get_app_id()
APP_IP = user.get_app_ip()

def load():
    read_res = r.request.read(APP_ID)

    # general errors
    if isinstance(read_res, Exception):
        print(f"Network or connection error during update: {read_res}")

    # not found
    elif read_res.status_code == 404:
        pass

    # other errors
    elif read_res.status_code not in (200, 204):
        print(f"Update failed with HTTP {read_res.status_code}: {read_res.text}")

    # Success
    else:
        data = json.load(read_res)
        print(data)
        # app_state.dash_row_values = data['json_values']
        # app_state.dash_rows = data['rows']
        print("Load successful.")
    
