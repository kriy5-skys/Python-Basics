import requests
import json
token = "56733325f371c9f4-ee3da6d379306a5a-e9b01773157d5e68"
super_admin_id = "dYmGbJqju+/IlUY4B4vUOw=="

def set_web_hook():
    url = "https://chatapi.viber.com/pa/set_webhook"
    payload = {
    "url":"https://www.broadwayinfosys.com", 
    "auth_token":token
    }
    r = requests.post(url = url, data = json.dumps(payload))
    print(r.json())

set_web_hook()

# {'status': 1}
# Error codes are given accordingly.

def get_account_info():
    url = "https://chatapi.viber.com/pa/get_account_info"
    payload = {
        "auth_token": token
    }
    r = requests.post(url = url, data = json.dumps(payload))
    print(r.json())

get_account_info()

def send_text_message():
    url = "https://chatapi.viber.com/pa/post"
    payload = {
        "auth_token": token,
        "from":super_admin_id, 
        "type":"text", 
        "text":"Hello world from python code, to you" 
    }
    r = requests.post(url = url, data = json.dumps(payload))
    print(r.json())

send_text_message()

def send_picture_message():
    url = "https://chatapi.viber.com/pa/post"
    payload = {
        "auth_token": token,
        "from":super_admin_id, 
        "type":"picture", 
        "text":"This is for Motivation", 
        "media":"https://broadwayinfosys.com/uploads/courses/31561776920552.webp", 
        "thumbnail":"https://broadwayinfosys.com/uploads/courses/31561776920552.webp" 
    }
    r = requests.post(url = url, data = json.dumps(payload))
    print(r.json())

send_picture_message()
