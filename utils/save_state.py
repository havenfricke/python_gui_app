import json
import app_state

def save_state():

    if app_state.dash_row_values:
        json_values = json.dumps(app_state.dash_row_values, indent=4)
        print(json_values)  

    if app_state.dash_rows >= 0:
        data = {
            "rows": app_state.dash_rows
        }
        json_values = json.dumps(data, indent=4)
        print(json_values)

