from slimgui import imgui
import app_state
from controllers.settings_controller import settings_ctrl

def init_settings():
    
    imgui.text_wrapped("Settings Configuration")
    changed, is_enabled = imgui.checkbox("Enable Dark Mode", app_state.watcher.dark_mode_enabled)

    if changed: 
        settings_ctrl.update_settings(is_enabled)