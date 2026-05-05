import os
import json
import string
import urllib.request
import secrets

def init_user_data():
    # default folder name should be "user_data"
    path = os.getcwd() + "/user_data"

    if os.path.isdir("user_data"):
        with open(path + '/user_data.json', 'r') as file:
            # Parse JSON into a Python dictionary
            data = json.load(file)
            # Access the specific key
            print("[APPLICATION ID]: " + data['app_id'])

    else:
        print(path)
        os.mkdir(path)
        
        chars = string.ascii_uppercase + string.digits
        ip_res = get_public_ip_standard()
        data = {
            "app_id": "-".join("".join(secrets.choice(chars) for _ in range(5)) for _ in range(10)),
            "current_ip": ip_res
        }

    with open(path + '/user_data.json', "w", encoding="utf-8") as f:
        f.write
        json.dump(data, f, indent=4)

    return path

def get_public_ip_standard():
    # ident.me is a simple service that returns your IP as plain text
    with urllib.request.urlopen('https://ident.me') as response:
        return response.read().decode('utf8')
    

def get_app_id():
    path = os.getcwd() + "/user_data"

    if os.path.isdir("user_data"):
        with open(path + '/user_data.json', 'r') as file:
            # Parse JSON into a Python dictionary
            data = json.load(file)
            # Access the specific key
            return data['app_id']
        
def get_app_ip():
    path = os.getcwd() + "/user_data"

    if os.path.isdir("user_data"):
        with open(path + '/user_data.json', 'r') as file:
            # Parse JSON into a Python dictionary
            data = json.load(file)
            # Access the specific key
            return data['current_ip']
    

