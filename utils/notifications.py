from slimgui import imgui

def extra_window(is_open: bool, title: str, content: str) -> tuple[bool, bool]:

    if not is_open:
        return False, False
    
    imgui.set_next_window_size((400.0, 200.0), imgui.Cond.FIRST_USE_EVER)

    expanded, currently_open = imgui.begin(title, True)

    proceed = False
    
    if expanded:

        imgui.text_wrapped(content)
        
        imgui.spacing()
        
        if imgui.button("OK"):
            proceed = True
            currently_open = False

        if imgui.button("Cancel"):
            proceed = False
            currently_open = False

            
    imgui.end()
    
    return currently_open, proceed # currently_open = window status, proceed = helper bool for calling extra_window()