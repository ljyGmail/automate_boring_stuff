import pyautogui
import time

# Clicking the Mouse
# pyautogui.click(10, 5)  # Move mouse to (10, 5) and click.
# pyautogui.click(800, 200, button='right')

# Dragging the Mouse
# time.sleep(5)
# pyautogui.click()  # Click to make the window active.
# distance = 300
# change = 20
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2)  # Move right.
#     distance -= change
#     pyautogui.drag(0, distance, duration=0.2)  # Move down.
#     pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
#     distance -= change
#     pyautogui.drag(0, -distance, duration=0.2)  # Move up.

pyautogui.scroll(100)
