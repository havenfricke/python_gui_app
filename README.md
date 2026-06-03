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

When the application first runs it will create a folder and file named `user_data/user_data.json` storing a uniquely generated ID and public IP address.
This information is used to identify app data ownership. The public IP address is fetched on app startup and cross-referenced with the last stored IP then, saved if different.

### Structure

![Alt Text](https://github.com/havenfricke/python_gui_app/blob/main/app_structure.png)


**What data should I be sending and receiving from my server?**
```sql
CREATE TABLE apps (
    app_id VARCHAR(255) NOT NULL PRIMARY KEY UNIQUE COMMENT 'Primary Key',
    app_ip VARCHAR(255) NOT NULL,
    app_metadata JSON
)
```
```python
class App:
    def __init__(self, app_id: str, app_ip: str, app_metadata: dict):
        self.app_id = app_id
        self.app_ip = app_ip
        self.app_metadata = app_metadata
```

*All necessary window objects, glfw, and imgui settings need to be passed as arguments to pages and components.*

