# run only if we're main console

if [ "$(tty)" = "/dev/tty1" ]; then
  $HOME/ipcam_kiosk/touch_reader.sh
  cmatrix

else
  echo "not console"
fi
