import pyautogui
import time

# Set the delay between clicks to achieve 150 clicks per second
click_delay = 1/150  # Calculating the delay for 150 clicks per second

def autoclicker(interval):
    try:
        while True:
            pyautogui.click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Autoclicker stopped.")

# Start the autoclicker
autoclicker(click_delay)
