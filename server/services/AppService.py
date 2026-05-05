from models.App import App
from repositories.AppRepository import app_repo

class AppService:

    def create_app(self, body: dict) -> App:
        created = app_repo.create_app(body)
        # 'created' evaluates to a dictionary
        return App(created['app_id'], created['app_metadata'], created['app_rows'])

    def get_all_apps(self) -> list[App]:
        apps = app_repo.get_all_apps()
        # 'prop' evaluates to a dictionary during each iteration
        return [App(prop['app_id'], prop['app_metadata'], prop['app_rows']) for prop in apps]

    def get_app_by_id(self, id: str) -> App:
        app = app_repo.get_app_by_id(id)

        if not app:
            raise ValueError("404: Example not found")
        
        # 'app' evaluates to a dictionary
        return App(app['app_id'], app['app_metadata'], app['app_rows'])

    def edit_app(self, id: str, update: dict) -> App:
            original = app_repo.get_app_by_id(id)

            if not original:
                raise ValueError("404: App not found")
                
            updated = {
                "app_metadata": original['app_metadata'] if update.get("app_metadata") == original['app_metadata'] else update.get("app_metadata"),
                "app_rows": original['app_rows'] if update.get("app_rows") == original['app_rows'] else update.get("app_rows")
                # Other props here if model allows
            }

            # Ensure the repository method also handles dictionaries correctly
            updated = app_repo.edit_app(original['app_id'], updated)
            
            # Remove [0] index here
            return App(updated['app_id'], updated['app_metadata'], updated['app_rows'])

    def delete_app(self, id: str) -> dict:
        example = app_repo.get_app_by_id(id)

        if not example:
            raise ValueError("404: Example not found")
        message = app_repo.delete_app(id)
        return message

app_service = AppService() # singleton pattern in python