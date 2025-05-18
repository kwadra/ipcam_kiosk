#!/bin/sh

export DISPLAY=:0
SCRIPT_HOME=$HOME/ipcam_kiosk
. ${SCRIPT_HOME}/venv/bin/activate
nohup ${SCRIPT_HOME}/touch_reader.py >/dev/null 2>&1 &
