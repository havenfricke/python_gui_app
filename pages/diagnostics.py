import glfw
from slimgui import imgui

def init_diagnostics(width, height, window):
    
    imgui.text("System Diagnostics")
    imgui.text(f"Logical Window Size: {width}x{height}")
    imgui.text(f"Framerate: {imgui.get_io().framerate:.1f} FPS")


    if imgui.button("Close Application", (150, 0)):
            glfw.set_window_should_close(window, True)