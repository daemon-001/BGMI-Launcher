killall -q com.pubg.imobile
am force-stop com.pubg.imobile
rm -rf /data/data/com.pubg.imobile/{shared_prefs,files,app_*,databases,cache,no_backup,code_cache}
rm -rf /storage/emulated/0/Android/data/com.pubg.imobile/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Logs/ShadowTrackerExtra.log
rm -rf /storage/emulated/0/Android/data/com.pubg.imobile/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/SaveGames/Active.sav
rm -rf /storage/emulated/0/Android/data/com.pubg.imobile/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/{UserSettings.ini,UserCustom.ini}
#chmod 777 /data/local/tmp/log_clear.sh && /data/local/tmp/log_clear.sh
#unzip /data/local/tmp/files.zip -d /data/data/com.pubg.imobile/
cp /data/local/tmp/ShadowTrackerExtra.log /storage/emulated/0/Android/data/com.pubg.imobile/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Logs/
cp /data/local/tmp/Active.sav /storage/emulated/0/Android/data/com.pubg.imobile/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/SaveGames/
cp /data/local/tmp/{UserSettings.ini,UserCustom.ini} /storage/emulated/0/Android/data/com.pubg.imobile/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/
am start -n com.pubg.imobile/com.epicgames.ue4.SplashActivity
