from fastapi import Request
from models.AppBody import AppBody
from utils.BaseController import BaseController
from services.AppService import app_service

class AppController(BaseController):
    def __init__(self):
        super().__init__("/apps")

        self.router.add_api_route("", self.create_app, methods=["POST"])
        self.router.add_api_route("", self.get_all_apps, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_app_by_id, methods=["GET"])
        self.router.add_api_route("/{id}", self.edit_app, methods=["PUT"])
        self.router.add_api_route("/{id}", self.delete_app, methods=["DELETE"])


    def create_app(self, body: AppBody):
        new_app = app_service.create_app(body.model_dump())
        return { "data": new_app }
    

    def get_all_apps(self):
        apps = app_service.get_all_apps()
        return { "data": apps }
    

    def get_app_by_id(self, id: str):
        app = app_service.get_app_by_id(id)
        return { "data": app }
    

    def edit_app(self, id: str, body: AppBody):
        app = app_service.edit_app(id, body.model_dump())
        return { "data": app }
    

    def delete_app(self, id: str):
        app = app_service.delete_app(id)
        return { "data": app }
        
app_controller = AppController() # singleton pattern in python