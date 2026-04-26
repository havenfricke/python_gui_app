from slimgui import imgui

def init_diagnostics(width, height):
    imgui.text("System Diagnostics")
    imgui.text(f"Logical Window Size: {width}x{height}")
    imgui.text(f"Framerate: {imgui.get_io().framerate:.1f} FPS")