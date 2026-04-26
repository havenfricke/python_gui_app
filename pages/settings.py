from slimgui import imgui
import app_state

def init_settings():
    imgui.text("Settings Configuration")
    changed, app_state.dark_mode_enabled = imgui.checkbox("Enable Dark Mode", app_state.dark_mode_enabled)