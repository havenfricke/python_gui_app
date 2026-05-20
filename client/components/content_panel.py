from slimgui import imgui
import app_state
import pages.dashboard as dashboard
import pages.settings as settings
import pages.conversations as conversations

def init_content_panel(width, height, window):

    imgui.begin_child("Content", (0, 0))

    match app_state.watcher.current_page:

        case "Dashboard":
           dashboard.init_dashboard()
        
        case "Settings":
            settings.init_settings()
        
        case "Conversations":
            conversations.init_conversations(width, height, window)

    imgui.spacing()

    imgui.end_child()