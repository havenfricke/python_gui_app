import app_state

class settings_controller:
    def __init__(self):
        pass
    
    def update_settings(self, dark_mode_enabled: bool):
        print("[SETTINGS CONTROLLER]: Update")
        app_state.watcher.dark_mode_enabled = dark_mode_enabled


settings_ctrl = settings_controller()