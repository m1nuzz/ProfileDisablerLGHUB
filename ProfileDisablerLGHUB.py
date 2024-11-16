import pyautogui
import time
import keyboard  # For detecting key presses

# Wait a bit to allow the LGHUB window to open
time.sleep(3)  # Reduced wait time

# Approximate coordinates for the first game
game_x = 695  # X coordinate for the first game
game_y = 237  # Y coordinate for the first game

# Coordinates for the "Settings" button and the new "Control Settings" button
settings_button = (347, 524)  # Coordinates for the "Settings" button
control_settings_button = (554, 520)  # Coordinates for the "Control Settings" button
profile_switch_button = (223, 690)  # Coordinates for the profile switch button

# Function to check if the W key is pressed in any window
def check_stop_key():
    return keyboard.is_pressed('w')  # Returns True if the 'W' key is pressed

# Function to perform all the clicks
def perform_actions():
    # Click on the game (clicking the same coordinates for all games)
    game_pos = (game_x, game_y)  # Coordinates remain the same for all games
    pyautogui.moveTo(game_pos)
    pyautogui.click()

    # Click on "Settings"
    pyautogui.moveTo(settings_button)
    pyautogui.click()

    # Click on "Control Settings"
    pyautogui.moveTo(control_settings_button)
    pyautogui.click()

    # Click on the profile switch button
    pyautogui.moveTo(profile_switch_button)
    pyautogui.click()

# Infinite loop to perform actions
while True:
    # Check if the W key is pressed to stop the script
    if check_stop_key():
        print("Script stopped by pressing the 'W' key.")
        break  # Exit the loop if the 'W' key is pressed

    # Perform actions
    perform_actions()

    # Reduce the wait time between actions to 1 second
    time.sleep(1)  # 1 second delay between actions

    print("Process completed for the current game, continuing execution...")

print("Script finished.")