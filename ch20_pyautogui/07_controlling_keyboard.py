import pyautogui

# Sending a String from the Keyboard

# pyautogui.click(100, 200)
# pyautogui.write('Hello world!')
# pyautogui.write('Hello world!', interval=0.2)

# Key Names
# pyautogui.click(100, 200)
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

# print(f'keyboard keys: {pyautogui.KEYBOARD_KEYS}')

# Pressing and Releasing the Keyboard
# pyautogui.click(100, 200)
# pyautogui.keyDown('shift')
# pyautogui.press('4')
# pyautogui.keyUp('shift')

# Hotkey Combinations
pyautogui.click(100, 200)
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('a')
# pyautogui.keyUp('a')
# pyautogui.keyUp('ctrl')

pyautogui.hotkey('ctrl', 'a')
