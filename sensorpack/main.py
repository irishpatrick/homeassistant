#!/usr/bin/env python3

import integration
import sensors
import time

def main():
    sensors.setup()

    sensors.teardown()

if __name__ == "__main__":
    main()
