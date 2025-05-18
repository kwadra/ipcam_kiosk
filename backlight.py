#!/usr/bin/env python
# Test script for backlight changes
from rpi_backlight import Backlight
backlight = Backlight()
backlight.power              # query or set power (True or False)
backlight.brightness       # query or set level (0-100)
