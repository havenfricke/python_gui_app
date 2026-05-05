import json
from DB.connection import query

class AppRepository:
    def __init__(self):
        pass

    def create_app(self, body: dict):
        # Update syntax to %(param_name)s
        create = "INSERT INTO apps (app_id, app_metadata, app_rows) VALUES (%(app_id)s, %(app_metadata)s, %(app_rows)s)"
        
        # Serialize dict to JSON string for the MySQL JSON column
        if isinstance(body.get("app_metadata"), dict):
            body["app_metadata"] = json.dumps(body["app_metadata"])

        query(create, body)
        
        # Extract the ID from the body, as lastrowid fails on VARCHAR columns
        created_id = body["app_id"]
        select = "SELECT * FROM apps WHERE app_id = %(app_id)s"
        created = query(select, {"app_id": created_id})
        return created
    
    def get_all_apps(self):
        get_all = "SELECT * FROM apps"
        res = query(get_all)
        return res
    
    def get_app_by_id(self, id: str):
        get_by_id = "SELECT * FROM apps WHERE app_id = %(app_id)s"
        # Include the parameter dictionary
        res = query(get_by_id, {"app_id": id})
        return res[0]

    def edit_app(self, id: str, body: dict):
        edit = "UPDATE apps SET app_metadata = %(app_metadata)s, app_rows = %(app_rows)s WHERE app_id = %(app_id)s"
        
        if isinstance(body.get("app_metadata"), dict):
            body["app_metadata"] = json.dumps(body["app_metadata"])

        new_body = {
            "app_id": id,
            **body   # unpack the body into params w id
        }
        res = query(edit, new_body)
        return res[0]

    def delete_app(self, id: str):
        delete = "DELETE FROM apps WHERE app_id = %(app_id)s"
        res = query(delete, { "app_id": id })
        return "Successful deletion" if res.get("affected_rows", 0) > 0 else "ID not found"


app_repo = AppRepository() # singleton pattern in python