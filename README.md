Setup for a simple IPcam viewer using a Raspberry PI wall-mounted with this 3D print -
https://makerworld.com/en/models/1168686-wall-pi-5#profileId-1176615

Display will normally show the "cmatrix" screen saver but will stream the camera for 10 minutes
after it detects any screen touch.

# Setup
1. Start with Raspian OS Desktop installation, enable SSH
1. Run "sudo raspi-config"
1. Select 1. System Options,S5 Boot,B1 Console Text console
1. Select 1. System Options,S6 Auto Login
1. Clone this repo to "pi" user $HOME directory 
1. cd $HOME/ipcam_kiosk/ && ./setup_ipcam_kiosk.sh
1. If your dsi-display is upside down, update /boot/firmware/cmdline.txt by adding video= entry based on sample cmdline.txt in this repo 
1. Append profile-run.sh to your $HOME/.profile file `cat profile-run.sh >> $HOME/.profile` to auto-run our scripts
1. Setup .env with your rtsp stream details

# Configuration
Configure the script by creating a ".env" file in your script directory. 
```
rtsp_user="rtsp_user"
rtsp_password="_secret_"
rtsp_hostname="cam_host_or_ip"
rtsp_channel=1
rtsp_runtime=600
# This varies by raspberry pi model. For 3B it's event2, Rpi 4 was event4
touch_input_device=/dev/input/event2
```
