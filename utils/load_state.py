import json
import app_state
import utils.req_interface as r
import utils.user_data as user
from models.App import App

APP_ID = user.get_app_id()
APP_IP = user.get_app_ip()

def load():
    app = App(app_id=APP_ID, app_metadata=app_state.dash_row_values, app_rows=app_state.dash_rows)
    print(app.__dict__)
    
    read_res = r.request.read(APP_ID) 

    # General network errors
    if isinstance(read_res, Exception):
        print(f"Network or connection error during load: {read_res}")
        return

    # Handle Missing Resource: Attempt creation ONLY on 404
    if read_res.status_code == 404:
        print(f"App ID {APP_ID} not found. Attempting to create...")
        
        create_res = r.request.create(app.__dict__)
        if create_res.status_code not in (200, 201, 204):
             print(f"CREATE failed with HTTP {create_res.status_code}: {create_res.text}")
             return
             
        # Read again after successful creation
        read_res = r.request.read(APP_ID)
        if read_res.status_code not in (200, 204):
            print(f"Subsequent load failed with HTTP {read_res.status_code}: {read_res.text}")
            return

    # Handle Server Errors (500) or other unhandled failure states
    elif read_res.status_code not in (200, 204):
        print(f"Load failed with HTTP {read_res.status_code}: {read_res.text}")
        
        create_res = r.request.create(app.__dict__)
        if create_res.status_code not in (200, 201, 204):
             print(f"CREATE failed with HTTP {create_res.status_code}: {create_res.text}")
             return
        
        return
       

    # Success Path (Guaranteed 200 or 204 at this point)
    try:
        data = json.loads(read_res.text)
        print(data)
        
        # Safely extract data, falling back to empty dicts if 'data' is missing
        payload = data.get('data', {})
        
        # --- Metadata Parsing Logic Applied Here ---
        raw_metadata = payload.get('app_metadata', {})

        # Ensure the metadata is parsed into a dictionary if it arrives as a string
        if isinstance(raw_metadata, str):
            try:
                app_state.dash_row_values = json.loads(raw_metadata)
            except json.JSONDecodeError:
                print("Warning: Failed to decode app_metadata. Defaulting to empty dict.")
                app_state.dash_row_values = {}
        else:
            app_state.dash_row_values = raw_metadata
        # -------------------------------------------
        
        app_state.dash_rows = payload.get('app_rows', 0)
        print("Load successful.")
        
    except json.JSONDecodeError:
        print("Failed to decode JSON from successful response.")
    except Exception as e:
        print(f"Error parsing response data: {e}")