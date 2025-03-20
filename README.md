# BGMI Launcher

A utility application to launch Battlegrounds Mobile India (BGMI) on LDPlayer emulator while bypassing emulator detection.


## Overview

BGMI Launcher provides a simple GUI interface to help players run BGMI on LDPlayer emulator by handling various bypass methods for emulator detection. The application streamlines the process of connecting to the emulator, managing network configurations, and launching the game with the right settings.

## 🔴Disclaimer

This project is for educational purposes only. Using emulators and bypass methods may violate the game's terms of service. Use at your own risk.


## Features

- **Connect Emulator**: Establishes ADB connection with LDPlayer and prepares the environment
- **Launch BGMI**: Starts the game with optimized settings and configurations
- **Reconnect Server**: Manages network connectivity to bypass server checks
- **Port Blocking**: Toggle network port blocking to prevent emulator detection
- **Clear Logs**: Removes game logs and cache files to avoid detection
- **Bottom Logbox**: Display all logs of scripts

## Requirements

- Windows OS
- LDPlayer Emulator (v4.0+ recommended)
- ADB (Android Debug Bridge)
- Python 3.x with customtkinter module

## Installation

1. Clone this repository or download the zip file
2. Install the required Python packages:
   ```
   pip install customtkinter
   ```
3. Make sure LDPlayer is installed in the default location or update the paths in the batch files
4. Run the launcher:
   ```
   python BGMI_Launcher.py
   ```
   
## File Structure

```
BGMI_Launcher/
│
├── BGMI_Launcher.py         # Main Python application file
├── BGMI_Launcher.exe        # Executable application file
├── icon.ico                 # Application icon
│
└── scripts/                    # Batch scripts & adb directory
    │
    ├── adb.exe                 # Adb driver pre included
    ├── fastboot.exe            # Adb driver pre included
    ├── AdbWinApi.dll           # Adb driver pre included
    ├── AdbWinUsbApi.dll        # Adb driver pre included
    │
    ├── connect_emulator.bat    # Script to connect to LDPlayer via ADB
    ├── lounch_bgmi.bat         # Script to launch BGMI with bypass settings
    ├── reconnect_server.bat    # Script to manage network connectivity
    ├── clear_logs.bat          # Script to clean game logs and cache
    ├── on.bat                  # Script to enable port blocking
    ├── off.bat                 # Script to disable port blocking
    │
    └── nmod                        # Configuration files archive
        │
        ├── ShadowTrackerExtra.log  # Placeholder log file
        ├── Active.sav              # Game save file
        ├── UserSettings.ini        # Modified game settings
        └── UserCustom.ini          # Custom game configuration
```   

## Usage

1. Start LDPlayer emulator
2. Launch the BGMI Launcher application
3. Click "Connect Emulator" to establish connection
4. Toggle "Port Block" if needed to bypass detection
5. Click "Launch BGMI" to start the game
6. If you experience connection issues, use "Reconnect Server"
7. Use "Clear Logs" periodically to avoid detection based on log files

## How It Works

The launcher uses a combination of techniques to bypass BGMI's emulator detection:

- Manages iptables rules to block specific ports used for detection
- Cleans game logs and cache files that might contain emulator information
- Handles network connectivity to prevent server-side detection
- Replaces certain game files with modified versions to bypass client-side checks

## Project Image
![image](https://github.com/user-attachments/assets/560049da-15b1-48cd-8ae1-fab75d22b6ca)



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
