import glfw
from slimgui import imgui

def init_diagnostics(width, height, window):
    
    imgui.text_wrapped("System Diagnostics")
    imgui.text_wrapped(f"Logical Window Size: {width}x{height}")
    imgui.text_wrapped(f"Framerate: {imgui.get_io().framerate:.1f} FPS")

    avail_width = imgui.get_content_region_avail()[0]

    button_width = min(150.0, avail_width)

    if imgui.button("Close Application", (button_width, 0)):
            glfw.set_window_should_close(window, True)