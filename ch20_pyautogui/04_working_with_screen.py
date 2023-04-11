import pyautogui
im = pyautogui.screenshot()

print(f'colort at (0, 0): {pyautogui.pixel(0, 0)}')
print(f'colort at (50, 200): {pyautogui.pixel(50, 200)}')

print(pyautogui.pixelMatchesColor(50, 200, (51, 51, 51)))
print(pyautogui.pixelMatchesColor(50, 200, (100, 120, 150)))
