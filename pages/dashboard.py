from slimgui import imgui
from app_state import dash_row_1_input

def init_dashboard():
    global dash_row_1_input
    avail_width = imgui.get_content_region_avail()[0]
    # text wrapped creates responsive text that will adapt to window size 
    imgui.text_wrapped("Dashboard View")
    imgui.text_wrapped("Welcome to the primary overview.")


    # Entire grid size is fed width and height of window (params, args)
    if imgui.begin_table(
            str_id="dash_grid_layout",
            column=3,
            flags=imgui.TableFlags.BORDERS,
            outer_size= (avail_width, 0),
            inner_width= 0.0
        ):

        imgui.table_next_column()
        imgui.table_set_column_index(0)

        imgui.text_wrapped("Label 1")

        imgui.table_next_column()
        imgui.table_set_column_index(1)

        changed, dash_row_1_input["value"] = imgui.input_text("", dash_row_1_input["value"])
        imgui.same_line()
        pressed_save = imgui.button("Save")

        if pressed_save:
            dash_row_1_input["saved"] = dash_row_1_input["value"]
            dash_row_1_input["value"] = ""

        imgui.table_next_column()
        imgui.table_set_column_index(2)
        
        pressed_rm = imgui.button("Clear")
        imgui.same_line()
        imgui.text_wrapped(dash_row_1_input["saved"])

        if pressed_rm:
            dash_row_1_input["saved"] = ""

        imgui.end_table()

    
        
