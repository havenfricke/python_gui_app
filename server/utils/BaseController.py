from fastapi import APIRouter

class BaseController:
    def __init__(self, mount: str):
        if not isinstance(mount, str) or not mount:
            raise ValueError("[BASECONTROLLER REGISTRATION ERROR]: No specified path")
        
        if not mount.startswith("/"):
            mount = "/" + mount

        self.mount = mount

        self.router = APIRouter(prefix=self.mount)