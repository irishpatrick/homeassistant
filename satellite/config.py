#!/usr/bin/env python3

import json
import pickle
import os
import base64

import integration

class DeviceInfo:
    def __init__(self):
        pass

class Registration:
    def __init__(self, obj):
        self.cloudhook_url = None
        self.remote_ui_url = None
        self.secret = None
        self.webhook_id = None

        if len(obj) > 0:
            self.extract_data(obj)

    def extract_data(self, obj):
        data = json.loads(obj)

        self.cloudhook_url = data["cloudhook_url"]
        self.remote_ui_url = data["remote_ui_url"]
        self.secret = data["secret"]
        self.webhook_id = data["webhook_id"]

    def get_secret(self):
        return base64.b64decode(self.secret)

    def get_webhook_url(self):
        return "http://0.0.0.0:8123/api/webook/{}".format(self.webhook_id)

def get_registration():
    if os.path.exists("./integration"):
        print("loading registration...")
        with open("./integration", "rb") as fp:
            return pickle.load(fp)

    else:
        print("registering device...")
        data = Registration(integration.register_device())
        with open("./integration", "wb") as fp:
            pickle.dump(data, fp)

