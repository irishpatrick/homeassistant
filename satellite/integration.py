#!/usr/bin/env python3

import json
import requests
import os
import nacl.secret
import nacl.utils

TESTTOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI4ZjEzZDhmOGQ3ODU0YjhjYjY3YTg3NmMyYzQ0N2VmMSIsImlhdCI6MTY1NDI2NTU0NSwiZXhwIjoxOTY5NjI1NTQ1fQ.duglwhtB4sqyKU4NdSYNZjE_5mhVRJ8Pn5D4hCmoYa0"
LONGTOKEN = "HASS_LL_TOKEN"
ADDR = "0.0.0.0"
PORT = "8123"
try:
    TESTING = os.environ["TEST"]
except:
    TESTING = False

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

def register_device():
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

    return response.text

def send_encrypted_data(data, reg):
    packet = {}
    
    message = bytes(json.dumps(data), "utf-8")
    print(len(reg.get_secret()))
    box = nacl.secret.SecretBox(reg.get_secret())
    cipher = box.encrypt(message)

    packet["type"] = "encrypted"
    packet["encrypted"] = True
    packet["encrypted_data"] = cipher

    response = requests.request("POST", reg.get_webhook_url(), json=packet)

    print(response.text)