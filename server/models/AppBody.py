from pydantic import BaseModel

class AppBody(BaseModel):
        app_id: str
        app_metadata: dict
        app_rows: int