import sys
import glfw
import OpenGL.GL as gl

from slimgui import imgui
from slimgui.integrations.glfw import GlfwRenderer

import components.nav as nav
import components.content_panel as content_panel

class window:
    def __init__(self, width: int = 800, height: int = 600, title: str = "ImGui Layout Example"):
        self.width = width
        self.height = height
        self.title = title
        
        self.window = self.init_glfw()
        self.impl = self.init_imgui()
        
        self.window_flags = (
            imgui.WindowFlags.NO_TITLE_BAR |
            imgui.WindowFlags.NO_RESIZE |
            imgui.WindowFlags.NO_MOVE |
            imgui.WindowFlags.NO_COLLAPSE |
            imgui.WindowFlags.NO_BRING_TO_FRONT_ON_FOCUS
        )
        
        # Register callbacks to force rendering during OS-level blocking operations
        glfw.set_framebuffer_size_callback(self.window, self.on_resize)
        glfw.set_window_refresh_callback(self.window, self.on_refresh)

    def init_glfw(self):
        if not glfw.init():
            sys.exit(1)

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

        window = glfw.create_window(self.width, self.height, self.title, None, None)
        glfw.set_window_size_limits(window, self.width, self.height, glfw.DONT_CARE, glfw.DONT_CARE)

        if not window:
            glfw.terminate()
            sys.exit(1)

        glfw.make_context_current(window)
        return window
    
    def init_imgui(self) -> GlfwRenderer:
        imgui.create_context()
        imgui.get_io().ini_filename = None
        return GlfwRenderer(self.window)
    
    def sync_io(self) -> tuple[int, int, int, int]:
        io = imgui.get_io()
        width, height = glfw.get_window_size(self.window)
        fb_width, fb_height = glfw.get_framebuffer_size(self.window)
        
        io.display_size = (width, height)

        if width > 0 and height > 0:
            io.display_framebuffer_scale = (fb_width / width, fb_height / height)
            
        return width, height, fb_width, fb_height
    
    def render_ui(self, width: int, height: int):
        imgui.set_next_window_pos((0, 0), imgui.Cond.ALWAYS)
        imgui.set_next_window_size((width, height), imgui.Cond.ALWAYS)

        imgui.push_style_var(imgui.StyleVar.WINDOW_ROUNDING, 0.0)
        imgui.push_style_var(imgui.StyleVar.WINDOW_BORDER_SIZE, 0.0)

        imgui.begin("Main", flags=self.window_flags)
        
        nav.init_nav()
        imgui.same_line()
        content_panel.init_content_panel(width, height, self.window)
            
        imgui.end()
        imgui.pop_style_var(2)

    def render_frame(self):
        # Isolated rendering pipeline
        width, height, fb_width, fb_height = self.sync_io()

        # Prevent rendering errors if the window is minimized (width or height becomes 0)
        if width == 0 or height == 0:
            return

        imgui.new_frame()
        self.render_ui(width, height)

        gl.glViewport(0, 0, fb_width, fb_height)
        gl.glClearColor(0.1, 0.15, 0.2, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        
        imgui.render()
        self.impl.render(imgui.get_draw_data())
        glfw.swap_buffers(self.window)

    def on_resize(self, window, width, height):
        self.render_frame()

    def on_refresh(self, window):
        self.render_frame()

    def run(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            self.render_frame()

        self.shutdown()

    def shutdown(self):
        self.impl.shutdown()
        glfw.terminate()