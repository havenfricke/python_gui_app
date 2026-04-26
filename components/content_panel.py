import app_state
import pages.dashboard as dashboard
import pages.settings as settings
import pages.diagnostics as diagnostics

def init_content_panel(width, height):

    match app_state.current_page:

        case "Dashboard":
            dashboard.init_dashboard()
        
        case "Settings":
            settings.init_settings()
        
        case "Diagnostics":
            diagnostics.init_diagnostics(width, height)