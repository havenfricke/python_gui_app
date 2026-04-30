from slimgui import imgui
from app_state import dash_row_values, dash_rows

def init_dashboard():
    global dash_row_values
    global dash_rows
    avail_width = imgui.get_content_region_avail()[0]
    
    imgui.text_wrapped("Dashboard View")
    imgui.text_wrapped("Welcome to the primary overview.")
    
    pressed_add_row = imgui.button("Add Row...") 
    imgui.same_line()
    imgui.text_wrapped(str(dash_rows))

    if pressed_add_row:
        dash_rows += 1
# ----------------------------------------

    

    for i in range(dash_rows):
        
        if f"value-{i}" not in dash_row_values:
            dash_row_values[f"value-{i}"] = ""
        if f"saved-{i}" not in dash_row_values:
            dash_row_values[f"saved-{i}"] = ""

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
            imgui.text_wrapped(f"Input {i + 1}")
            imgui.same_line()
            
            # Flag the row for removal, do NOT delete data here
            pressed_rm_row = imgui.button(f"Remove##rm_{i}")
            if pressed_rm_row:
                row_to_remove = i

            imgui.table_next_column()
            imgui.table_set_column_index(1)

            changed, dash_row_values[f"value-{i}"] = imgui.input_text(f"##input_{i}", dash_row_values[f"value-{i}"])
            imgui.same_line()
            
            pressed_save = imgui.button(f"Save##save_{i}")

            if pressed_save:
                dash_row_values[f"saved-{i}"] = dash_row_values[f"value-{i}"]
                dash_row_values[f"value-{i}"] = ""

            imgui.table_next_column()
            imgui.table_set_column_index(2)
            
            pressed_clear = imgui.button(f"Clear##clr_{i}")
            imgui.same_line()
            imgui.text_wrapped(dash_row_values[f"saved-{i}"])

            if pressed_clear:
                dash_row_values[f"saved-{i}"] = ""

            imgui.end_table()

    # Handle the deletion
    if row_to_remove is not None:
        # Shift all subsequent values down by 1 index to fill the gap
        for j in range(row_to_remove, dash_rows - 1):
            dash_row_values[f"value-{j}"] = dash_row_values[f"value-{j + 1}"]
            dash_row_values[f"saved-{j}"] = dash_row_values[f"saved-{j + 1}"]
        
        # Delete the final duplicate keys at the end of the shifted dictionary
        last_index = dash_rows - 1
        del dash_row_values[f"value-{last_index}"]
        del dash_row_values[f"saved-{last_index}"]
        
        dash_rows -= 1