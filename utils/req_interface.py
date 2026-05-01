import requests

# Changed to http:// - adjust back to https:// only if your local server uses SSL
BASE_URL = "http://localhost:8000"


class req_interface:
    def __init__(self):
        pass

    def create(self, data):
        try:
            res = requests.post(BASE_URL, json=data)
            
            print(f"CREATE: Status {res.status_code}, Data: {res.json()}")
            return res
        except requests.exceptions.RequestException as e:
            print(f"CREATE Request Failed: {e}")
            return e

    def read(self, id=None):
        try:
            url = f"{BASE_URL}/{id}" if id else BASE_URL
            res = requests.get(url)
            if res.status_code == 200:
                print(f"READ: {res.json()}")
            return res
        except requests.exceptions.RequestException as e:
            print(f"READ Request Failed: {e}")
            return e
        
    def update(self, id, data): 
        try:
            res = requests.put(f"{BASE_URL}/{id}", json=data)
            if res.status_code == 200:
                print(f"UPDATE: Status {res.status_code}, Data: {res.json()}")
            return res
        except requests.exceptions.RequestException as e:
            print(f"UPDATE Request Failed: {e}")
            return e

    def delete(self, id): 
        try:
            res = requests.delete(f"{BASE_URL}/{id}")
            if res.status_code in (200, 204):
                print(f"DELETE: Status {res.status_code} (Success)")
            return "Successful deletion"
        except requests.exceptions.RequestException as e:
            print(f"DELETE Request Failed: {e}")
            return e
        
request = req_interface()