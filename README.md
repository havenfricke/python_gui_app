### Getting started

**Python v3.10+ required for using `match` statements.**

### Structure

![Alt Text](/app_structure.png)

### Project Overview
python_gui_app is a Python-based scaffold framework designed for creating cross-platform, cloud-connected desktop applications with built-in state tracking. It utilizes slimgui (an ImGui binding) for the user interface.

**Prerequisites & Installation**
The framework relies heavily on Python 3.10+ *to support modern language features like match statements*.

Dependencies: slimgui, glfw, PyOpenGL, numpy, requests

**Setup Instructions:**

- Create a virtual environment: python -m venv venv_name

- Activate the virtual environment:

- Windows: `./venv_name/Scripts/Activate.ps1`

- Linux/macOS: `source venv_name/bin/activate`

- Install required packages: `pip install slimgui glfw PyOpenGL numpy requests`

**Architectural Documentation**
The framework implements a strict component-based architecture. To maintain stability, modifications should be isolated to specific directories.

1. Core Entry Point (main.py)
Purpose: Serves strictly as the runtime entry point.

Usage constraint: This file should not be extended, modified, or populated with application logic. It solely triggers the initialization sequence.

2. Window & Application Structure (core/window.py)
Purpose: Handles the primary GLFW window initialization, application loop, general rendering settings, and structural layout definitions.

Usage: Window objects, GLFW context configurations, and ImGui rendering loops are managed here. All subsequent UI components rely on context defined in this file.

3. State Management (app_state.py)
Purpose: A centralized data store used to house variables, arrays, and application states.

Usage: Any file needing to write or read application-level variables must import and interface with app_state.py. This ensures a uniform state and prevents prop-drilling or circular dependency issues between nested GUI elements.

4. UI Components (/components/)
Purpose: Houses modular GUI layout constructs.

nav.py: Responsible for managing the sidebar/topbar navigation menu events and rendering.

content_panel.py: Responsible for dynamically mounting and unmounting page views within the central application frame.

Usage constraint: When modifying or creating new components, you must pass the active window objects, GLFW context, and ImGui settings as function/method arguments.

5. Application Views (/pages/)
Purpose: Houses the distinct user-facing screens of the application.

Usage: Files placed here represent specific views that are rendered inside the content_panel when triggered by nav.py.

Data Initialization and Cloud Tracking Protocol
Local Identity File:
Upon first execution, the application automatically provisions a local JSON file at user_data/user_data.json.

It generates and stores a unique Application ID string.

It fetches the public IP of the host machine. On subsequent boots, the public IP is cross-referenced with the stored IP and rewritten if a change is detected.

Server/Database Synchronization Setup:
The scaffold is designed to push this local identity to a backend server. The developer is instructed to mirror the local data model using the following backend architecture:

SQL Schema for App Tracking:

```SQL
CREATE TABLE apps (
    app_id VARCHAR(255) NOT NULL PRIMARY KEY UNIQUE COMMENT 'Primary Key',
    app_ip VARCHAR(255) NOT NULL,
    app_metadata JSON
)
Python Class Mapping Example (Backend/Server Code):
```
```Python
class App:
    def __init__(self, app_id: str, app_ip: str, app_metadata: dict):
        self.app_id = app_id
        self.app_ip = app_ip
        self.app_metadata = app_metadata
```
**Component Implementation Rule**
A critical enforcement rule defined by the architecture is that context is not globally inherited by the GUI elements. All necessary window objects, GLFW instances, and ImGui settings must be explicitly passed as arguments to any new pages and components you create.

