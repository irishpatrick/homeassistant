#!/usr/bin/env python3

import json
import requests
import os

TESTTOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI4ZjEzZDhmOGQ3ODU0YjhjYjY3YTg3NmMyYzQ0N2VmMSIsImlhdCI6MTY1NDI2NTU0NSwiZXhwIjoxOTY5NjI1NTQ1fQ.duglwhtB4sqyKU4NdSYNZjE_5mhVRJ8Pn5D4hCmoYa0"
LONGTOKEN = "HASS_LL_TOKEN"
ADDR = "0.0.0.0"
PORT = "8123"
try:
    TESTING = os.environ["TEST"]
except:
    TESTING = False

class Hook:
    def __init__(self, obj):
        self.cloudhook_url = None
        self.remote_ui_url = None
        self.secret = None
        self.webhook_id = None

        if len(obj) > 0:
            self.extract_data(obj)

    def extract_data(self, obj):
        data = json.loads(obj)

        self.cloudhook_url = data.cloudhook_url
        self.remote_ui_url = data.remote_ui_url
        self.secret = data.secret
        self.webhook_id = data.webhook_id

def get_endpoint(endpt):
    return "http://{}:{}{}".format(ADDR, PORT, endpt)

def build_header():
    if TESTING:
        tok = TESTTOKEN
    else:
        tok = os.environ[LONGTOKEN]

    return {"Authorization": "Bearer {}".format(tok)}

def get_config():
    url = get_endpoint("/api/config")
    headers = build_header()

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def register_device():
    # TODO check if device already registered, and skip if so

    url = get_endpoint("/api/mobile_app/registrations")
    headers = build_header()
    data = {
        "device_id": "satellite",
        "app_id": "satellite",
        "app_name": "Satellite",
        "app_version": "1.0.0",
        "device_name": "Pi Satellite",
        "manufacturer": "Raspberry Pi",
        "model": "Pi Zero W",
        "os_name": "raspbian",
        "os_version": "bullseye",
        "supports_encryption": "true",
        "app_data": {
            "push_notification_key": "abcdef"
        }
    }

    response = requests.request("POST", url, json=data, headers=headers)

    return Hook(response.text)
