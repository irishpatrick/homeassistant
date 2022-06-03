#!/usr/bin/env python3

import integration
import sensors
import time

def main():
    sensors.setup()

    integration.get_config()
    integration.register_device()

    sensors.teardown()

if __name__ == "__main__":
    main()
