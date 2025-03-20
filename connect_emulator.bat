adb kill-server
adb start-server
adb devices
adb connect 127.0.0.1:5555
adb shell su -c 'rm -rf /data/local/tmp/*'
adb push nmod /data/local/tmp/
adb shell su -c 'unzip /data/local/tmp/nmod -d /data/local/tmp/'
