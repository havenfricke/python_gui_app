### Getting started

**Python v3.10+ required for using `match` statements.**

- Create venv: `python -m venv venv_name`
- `cd venv_name` then (Windows) `./Scripts/Activate.ps1` or (Linux) `source bin/activate`
- Switch interpreter to venv if necessary.
- Install packages: `pip install slimgui glfw PyOpenGL numpy requests`
- [ImGui reference](https://nurpax.github.io/slimgui/api/imgui.html) (Have this open when building with this app)


### Overview

The main.py file is a simple entry point for the application. It is not meant to be extended, added to, or modified.
Inside `/core/window.py` is the main application layout and structure, window initialization, and other general settings.
The `/components/...` path contains layout elements such as `nav.py` and `content_panel.py`. They are responsible for handling
the navigation menu and dynamic "content panel" updates during app use. Inside `/pages/...` are the "pages" that are rendered
when navigating the application. The `app_state.py` file is responsible for housing variables, arrays, etc. for the state of the
application to remain uniform and allow any file to access values necessary for the application's functionality.


### Structure

- main.py / app_state.py -> /core -> /components -> /pages


*All necessary window objects, glfw, and imgui settings need to be passed as arguments to pages and components.*

