#!/bin/sh
# Simple test script to display rtsp feed from Dahua cam

export DISPLAY=:0
source ./.env
rtsp_channel=1

cvlc -v "rtsp://${rtsp_user}:${rtsp_password}@${rtsp_hostname}/cam/realmonitor?channel=1&subtype=${rtsp_channel}" \
#--run-time=600  vlc://quit
