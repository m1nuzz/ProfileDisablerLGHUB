# ProfileDisablerLGHUB

This Python script automates the process of disabling profile switching for all games in Logitech G Hub. It clicks through each game on the main page, opens settings, and disables the profile switch.

## Requirements

- **LGHUB window must be open in fullscreen**.
- **Full HD resolution (1920x1080)** is required.

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install required Python libraries:
    ```bash
    pip install pyautogui keyboard
    ```

## How It Works

1. The script clicks on each game on the main page of LGHUB.
2. It opens the settings for each game and disables the profile switch.
3. The script runs indefinitely, clicking through all games with a 1-second delay.
4. To stop the script, press the **W** key at any time.

## Usage

1. Open **LGHUB** in **fullscreen** with **1920x1080** resolution.
2. Run the script:
    ```bash
    python ProfileDisablerLGHUB.py
    ```
3. The script will begin clicking through games and disabling profile switching.
4. Press **W** to stop the script.

## Notes

- The script assumes the positions of the buttons and first game on the main page are fixed. Modify the script if your window layout differs.
- Only supports **Full HD** (1920x1080) resolution.
