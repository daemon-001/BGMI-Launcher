@REM adb shellsvc wifi disable && sleep 2 && svc wifi enable"

adb shell settings put global airplane_mode_on 1 && am broadcast -a android.intent.action.AIRPLANE_MODE
@REM adb shell su -c 'chmod 777 /data/local/tmp/log_clear.sh && /data/local/tmp/log_clear.sh'
@REM adb shell su -c 'unzip /data/local/tmp/files.zip -d /data/data/com.pubg.imobile/'
adb connect 127.0.0.1:5555
adb shellsettings put global airplane_mode_on 0 && am broadcast -a android.intent.action.AIRPLANE_MODE
@REM adb shellsvc wifi disable
@REM @REM ping -n 5 -w 500 127.0.0.1
@REM adb shellsvc wifi enable
