# BGMI Launcher

A utility application to launch Battlegrounds Mobile India (BGMI) on LDPlayer emulator while bypassing emulator detection.

![BGMI Launcher](https://placeholder-image-url.com/bgmi-launcher.png)

## Overview

BGMI Launcher provides a simple GUI interface to help players run BGMI on LDPlayer emulator by handling various bypass methods for emulator detection. The application streamlines the process of connecting to the emulator, managing network configurations, and launching the game with the right settings.

## Features

- **Connect Emulator**: Establishes ADB connection with LDPlayer and prepares the environment
- **Launch BGMI**: Starts the game with optimized settings and configurations
- **Reconnect Server**: Manages network connectivity to bypass server checks
- **Port Blocking**: Toggle network port blocking to prevent emulator detection
- **Clear Logs**: Removes game logs and cache files to avoid detection

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

## Disclaimer

This project is for educational purposes only. Using emulators and bypass methods may violate the game's terms of service. Use at your own risk.

## Contributing

Feel free to fork this project and submit pull requests with improvements or additional features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
