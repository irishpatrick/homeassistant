#!/usr/bin/env python3

import time

import integration
import sensors
import config

def main():
    sensors.setup()

    integration.get_config()
    reg = config.get_registration()

    testdata = {
        "type": "update-location",
        "data": {
            "gps": [12.34, 56.78],
            "gps_accuracy": 120,
            "battery": 69,
        }
    }
    integration.send_encrypted_data(testdata, reg)

    sensors.teardown()

if __name__ == "__main__":
    main()
