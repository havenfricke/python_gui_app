import json
import uuid
from models.App import App
from models.Message import Message
from utils.user_data import get_app_id, get_app_ip

# --- Custom JSON Encoder ---
class StateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return super().default(obj)

# --- Network Object ---
app: App = {}

# --- App State ---
app_metadata = {}

class Watcher:
    def __init__(self):
        self.__dict__['current_page'] = "Dashboard"
        self.__dict__['show_extra_window'] = False
        self.__dict__['extra_window_message'] = ""
        self.__dict__['username'] = "New User"
        self.__dict__['username_input'] = ""
        self.__dict__['dark_mode_enabled'] = True
        self.__dict__['current_chat'] = None
        self.__dict__['cc_messages'] = {}
        self.__dict__['message_input'] = None

    def __setattr__(self, name, value):
        current_value = self.__dict__.get(name)
        if current_value != value:
            self.__dict__[name] = value
            self.on_change(name, value)

    def on_change(self, name, new_value):
        global app_metadata
        global app
        
        app_metadata[name] = new_value
        
        # FIX: Pass the custom encoder to handle the Message and UUID objects
        change_json = json.dumps({name: new_value}, cls=StateEncoder)
        
        print(f"Triggered Update: {change_json}")

        # FIX: Pass the custom encoder here as well
        app = App(get_app_id(), get_app_ip(), json.dumps(app_metadata, cls=StateEncoder))
        
        print(f"app_id: {app.app_id},\napp_ip: {app.app_ip},\napp_metadata: {app.app_metadata}")

# ----- Example Usage -----
watcher = Watcher() # import app_state -> app_state.watcher.name_of_var_here

# # These assignments will automatically trigger __setattr__
# watcher.current_page = "Settings"
# watcher.dark_mode_enabled = False
# watcher.a_value_goes_here = 100

# # Assigning the same value does nothing (prevents redundant updates)
# watcher.current_page = "Settings"