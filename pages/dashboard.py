from slimgui import imgui
import app_state
from utils.save_state import save_state

def init_dashboard():
    # global row_to_remove
    # global dash_row_values
    # global dash_rows
    # global show_extra_window
    # global new_row_title

    avail_width = imgui.get_content_region_avail()[0]
    
    imgui.text_wrapped("Dashboard View")
    imgui.text_wrapped("Welcome to the primary overview.")
    
    pressed_add_row = imgui.button("Add Row...") 
    imgui.same_line()
    imgui.text_wrapped(str(app_state.dash_rows))

    if pressed_add_row:
        # Only open the window, do not increment dash_rows yet
        app_state.show_extra_window = True

    if app_state.show_extra_window:
        expanded, app_state.show_extra_window = imgui.begin("My Extra Window", closable=False)
        
        if expanded:
            imgui.text_wrapped("Enter Title for New Row:")
            
            changed, app_state.new_row_title = imgui.input_text("##row_title_input", app_state.new_row_title)

            if imgui.button("Save & Close"):
                app_state.dash_row_values[f"title-{app_state.dash_rows}"] = app_state.new_row_title
                
                app_state.dash_rows += 1
                
                app_state.new_row_title = ""
                
                app_state.show_extra_window = False

                save_state()

            imgui.same_line()

            if imgui.button("Cancel"):
                new_row_title = ""

                app_state.show_extra_window = False   
                    
        imgui.end()
# ----------------------------------------

    for i in range(app_state.dash_rows):
        
        if f"value-{i}" not in app_state.dash_row_values:
            app_state.dash_row_values[f"value-{i}"] = ""
        if f"saved-{i}" not in app_state.dash_row_values:
            app_state.dash_row_values[f"saved-{i}"] = ""
        # Fallback in case a row was created before this logic was added
        if f"title-{i}" not in app_state.dash_row_values:
            app_state.dash_row_values[f"title-{i}"] = f"Input {i + 1}"

        table_id = f"table_{i}"
        
        if imgui.begin_table(
            str_id=table_id,
            column=3,
            flags=imgui.TableFlags.BORDERS,
            outer_size=(avail_width, 0),
            inner_width=0.0
        ):

            imgui.table_next_column()
            imgui.table_set_column_index(0)
            
            # Display the dynamically saved title
            imgui.text_wrapped(app_state.dash_row_values[f"title-{i}"])
            imgui.same_line()
            
            # Flag the row for removal, do NOT delete data here
            pressed_rm_row = imgui.button(f"Remove##rm_{i}")
            if pressed_rm_row:
                app_state.row_to_remove = i

            imgui.table_next_column()
            imgui.table_set_column_index(1)

            changed, app_state.dash_row_values[f"value-{i}"] = imgui.input_text(f"##input_{i}", app_state.dash_row_values[f"value-{i}"])
            imgui.same_line()
            
            pressed_save = imgui.button(f"Save##save_{i}")

            if pressed_save:
                app_state.dash_row_values[f"saved-{i}"] = app_state.dash_row_values[f"value-{i}"]
                app_state.dash_row_values[f"value-{i}"] = ""
                save_state()

            imgui.table_next_column()
            imgui.table_set_column_index(2)
            
            pressed_clear = imgui.button(f"Clear##clr_{i}")
            imgui.same_line()
            imgui.text_wrapped(app_state.dash_row_values[f"saved-{i}"])

            if pressed_clear:
                app_state.dash_row_values[f"saved-{i}"] = ""
                save_state()

            imgui.end_table()

# ----------------------------------------

# Handle the deletion
    if app_state.row_to_remove is not None:
        # Shift all subsequent values down by 1 index to fill the gap
        for j in range(app_state.row_to_remove, app_state.dash_rows - 1):
            app_state.dash_row_values[f"value-{j}"] = app_state.dash_row_values[f"value-{j + 1}"]
            app_state.dash_row_values[f"saved-{j}"] = app_state.dash_row_values[f"saved-{j + 1}"]
            app_state.dash_row_values[f"title-{j}"] = app_state.dash_row_values[f"title-{j + 1}"] # Shift title
        
        # Delete the final duplicate keys at the end of the shifted dictionary
        last_index = app_state.dash_rows - 1
        del app_state.dash_row_values[f"value-{last_index}"]
        del app_state.dash_row_values[f"saved-{last_index}"]
        del app_state.dash_row_values[f"title-{last_index}"] # Delete title
        
        app_state.dash_rows -= 1
        
        # Reset the flag so it does not trigger again on the next frame
        app_state.row_to_remove = None
        
        save_state()

        