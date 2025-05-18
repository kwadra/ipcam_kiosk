#!/usr/bin/env python
from evdev import InputDevice, ecodes
from select import select
import os
import subprocess
import time
import logging
from dotenv import load_dotenv

load_dotenv()  # take environment variables

rtsp_user = os.getenv("rtsp_user")
rtsp_password = os.getenv("rtsp_password")
rtsp_hostname = os.getenv("rtsp_hostname")
rtsp_channel = os.getenv("rtsp_channel")
touch_input_device=os.getenv("touch_input_device")
dev = InputDevice(touch_input_device)

rtsp_url = f"rtsp://{rtsp_user}:{rtsp_password}@{rtsp_hostname}/cam/realmonitor?channel=1&subtype={rtsp_channel}"
cmd_line = ["cvlc",  "-v", rtsp_url, "--run-time=300" , "vlc://quit"]

while True:
   r,w,x = select([dev], [], [])
   for event in dev.read():
       logging.info(event)
       if time.time() - event.sec > 1.0:
          logging.info("skipping old event")
          continue
       result = subprocess.run(cmd_line, capture_output=True, text=True, check=True)
       logging.info(result.stdout)
       if event.type == ecodes.EV_ABS:
          if event.code == ecodes.ABS_X:
              x = event.value
              logging.info(f"X: {x}")
          elif event.code == ecodes.ABS_Y:
              y = event.value
              logging.info(f"Y: {y}")
