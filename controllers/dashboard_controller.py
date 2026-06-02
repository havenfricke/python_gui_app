import app_state
import re

class dashboard_controller:
    def __init__(self):
        pass

    def update_username_input(self, input_text: str):
        print("[CONVERSATION CONTROLLER]: update username input")
        app_state.watcher.username_input = input_text

    def update_username(self):
        print("[CONVERSATION CONTROLLER]: Update username")
        expected_characters = r'^[a-zA-Z0-9]+$' # expect only normal english letters and numbers
        if re.fullmatch(expected_characters, app_state.watcher.username_input) and app_state.watcher.username_input != app_state.watcher.username:
            app_state.watcher.username = app_state.watcher.username_input
            app_state.watcher.username_input = ""
        else:
            app_state.watcher.extra_window_message = f"{app_state.watcher.username_input} contains invalid characters or is already your username."
            app_state.watcher.show_extra_window = True
                        

dashboard_ctrl = dashboard_controller()