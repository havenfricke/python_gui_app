### Getting Started

Altered version of [python_webserver](https://github.com/havenfricke/python_webserver). Set up for [scalegrid.io](https://scalegrid.io/) MySql database.

- Get the latest version of python [here](https://www.python.org/downloads/) if you are on Windows.
- pip is included with the latest version of Python
- `git clone https://github.com/havenfricke/python_webserver.git`
- `cd python_webserver`
- `code .`
- Open the terminal in VS Code
- Run `python3 -m venv server_env` to create a python virtual environment
- Run `cd server_env` to change directory to the created environment
- (Linux) Run `source bin/activate` or (Windows) run `.\Scripts\Activate.ps1` to activate the Python environment
- Run `pip install fastapi` to install [FastAPI](https://fastapi.tiangolo.com/)
- Run `pip install uvicorn` to install [Uvicorn](https://uvicorn.dev/)
- Run `pip install dotenv` to install [dotenv](https://pypi.org/project/python-dotenv/)
- Run `pip install cryptography` to install [cryptography](https://pypi/project/cryptography/) (for dotenv)
- Run `pip install sqlalchemy` to install [SQLAlchemy](https://www.sqlalchemy.org/)
- Run `pip install aiomysql` to install [aiomysql](https://pypi.org/project/aiomysql/) (for SQLAlchemy to un async operations)
- Run `pip install pymysql` to install [pysql](https://pypi.org/project/pysql/)

*If you are on Windows the below steps are necessary*
- Switch Interpreters using VS Code shortcut: CTRL + SHIFT + P, type "python: select interpreter"
- Select the interpreter inside the server_env folder created using `python3 -m venv server_env` (You will get import errors if you do not)

- After environment set-up and package installations are complete, run `python main.py` from the root directory to start the server.

### Server Archtecture

**Controllers**: Responsible for incoming traffic, handling files, and authorization.

**DB**: Responsible for creating a pool connection to the MySQL database cluster and executing MySQL commands (Object relational mapping).

**Models**: Responsible for modeling known incoming and outgoing data structures, allowing control over what data is included in the application.

**Repositories**: Responsible for querying necessary MySQL logic related to the application's functionality (Object relational mapping).

**Services**: Responsible for additional logic necessary for the data to be well received by the repository and database.

**Utils**: Responsible for additional refactored code dump called upon by the core system.

**.env**: Responsible for housing and distributing sensitive information throughout the application (hidden during runtime).

*Before deploying this server, check main.py, DB/connection.py, and .env to update necessary security policies, environment variables, and configurations*

