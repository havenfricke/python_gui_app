from slimgui import imgui
import app_state
from utils.notifications import extra_window
from controllers.dashboard_controller import dashboard_ctrl

def init_dashboard():

    avail_width = imgui.get_content_region_avail()[0]
    
    imgui.text_wrapped("Dashboard View")
    imgui.text_wrapped(f"Welcome to the primary overview, {app_state.watcher.username}")
    imgui.spacing()
    imgui.text_wrapped("[USER SETTINGS]")

# ---------------------------------------- [TABLE 1]: Username Input

    if imgui.begin_table(
        str_id="username-input",
        column=2,
        flags=imgui.TableFlags.BORDERS,
        outer_size=(avail_width / 2.2, 0),
        inner_width=0.0
    ):

        imgui.table_setup_column(
            label="username-label", 
            flags=imgui.TableColumnFlags.WIDTH_FIXED, 
            init_width_or_weight=75
            )
        
        imgui.table_setup_column(
            label="username-label", 
            flags=imgui.TableColumnFlags.WIDTH_STRETCH, 
            init_width_or_weight=500
            )
        
        imgui.table_next_column()
        imgui.table_set_column_index(0)
        
        imgui.text_wrapped("Username:")

        imgui.table_next_column()
        imgui.table_set_column_index(1)

        changed, new_username = imgui.input_text("##username-input", app_state.watcher.username_input)

        if changed:
            dashboard_ctrl.update_username_input(new_username)

        imgui.same_line()

        pressed_update_username = imgui.button("Update", (avail_width / 10, 20))

        if pressed_update_username:
            
            app_state.watcher.extra_window_message = f"Are you sure you want to change your username to {app_state.watcher.username_input}?"
            app_state.watcher.show_extra_window = True


        if app_state.watcher.show_extra_window:
            app_state.watcher.show_extra_window, proceed = extra_window(
                is_open=app_state.watcher.show_extra_window,
                title="Change Username?",
                content=app_state.watcher.extra_window_message
            )

            if proceed:

                dashboard_ctrl.update_username()

                if app_state.watcher.show_extra_window:
                    app_state.watcher.show_extra_window, proceed = extra_window(
                        is_open=app_state.watcher.show_extra_window,
                        title="Invalid",
                        content=app_state.watcher.extra_window_message
                    )


        imgui.end_table()

# ---------------------------------------- [TABLE 1]: Username Input



        