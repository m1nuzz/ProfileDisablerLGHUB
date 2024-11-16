# LGHUB Profile Switcher Automation Script

This Python script automates the process of clicking through LGHUB (Logitech G Hub) to disable profile switching for all games on the main page. It will click through each game, open the settings, then disable the profile switch for that game. The script will continue running indefinitely until the "W" key is pressed, at which point the script will stop.

## Requirements

- **LGHUB window should be open in fullscreen** mode.
- The script supports **Full HD resolution (1920x1080)** only.

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install the required Python libraries:
    ```bash
    pip install pyautogui keyboard
    ```

## How It Works

1. The script first waits for the LGHUB window to be ready.
2. It clicks on the first game on the main page of LGHUB.
3. After selecting the game, the script clicks on the "Settings" button.
4. It then clicks on the "Control Settings" button and disables the profile switch for that game.
5. The script repeats the process for all games on the main page.
6. It continues this process indefinitely with a 1-second delay between actions.
7. Press the **W** key to stop the script at any time.

## Usage

1. Open the **LGHUB** window and make sure it's in **fullscreen** mode with a resolution of **1920x1080**.
2. Run the script using:
    ```bash
    python lghub_profile_switcher.py
    ```
3. The script will automatically start clicking through the games and disabling profile switching.
4. To stop the script, press the **W** key at any time.

## Notes

- The script only supports Full HD (1920x1080) resolution for the LGHUB window.
- The script assumes that the positions of the buttons (Settings, Control Settings, Profile Switch) and the first game on the main page are fixed. Adjustments may be needed if your window layout differs.
- If you need to adjust the positions of the buttons, modify the corresponding coordinates in the script.
