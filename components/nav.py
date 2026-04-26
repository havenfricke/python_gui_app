from slimgui import imgui
import app_state

def init_nav():
    imgui.begin_child("Navbar", (200, 0), imgui.ChildFlags.BORDERS)
    
    imgui.text("MENU")
    imgui.separator()

    if imgui.selectable("Dashboard", app_state.current_page == "Dashboard")[0]:
        app_state.current_page = "Dashboard"
        
    if imgui.selectable("System Settings", app_state.current_page == "Settings")[0]:
        app_state.current_page = "Settings"
        
    if imgui.selectable("Diagnostics", app_state.current_page == "Diagnostics")[0]:
        app_state.current_page = "Diagnostics"
        
    imgui.end_child()
