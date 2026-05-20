from slimgui import imgui
import app_state

def init_nav():
    
    imgui.begin_child("Navbar", (200, 0), imgui.ChildFlags.BORDERS)
    
    imgui.text("MENU")
    imgui.separator()

    if imgui.selectable("Dashboard", app_state.watcher.current_page == "Dashboard")[0]:
        app_state.watcher.current_page = "Dashboard"

    if imgui.selectable("Conversations", app_state.watcher.current_page == "Conversations")[0]:
        app_state.watcher.current_page = "Conversations"
        
    if imgui.selectable("System Settings", app_state.watcher.current_page == "Settings")[0]:
        app_state.watcher.current_page = "Settings"
        
    imgui.end_child()
