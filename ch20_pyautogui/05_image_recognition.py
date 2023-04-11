import pyautogui
import pyautogui

# b = pyautogui.locateOnScreen('data/include_cbx.png')
# print(f'b box: {b}')
# print(f'b[0]: {b[0]}')
# print(f'b.left: {b.left}')
# b2 = pyautogui.locateOnScreen('data/list_cbx.png')
# print(f'b2 box: {b2}')

print(list(pyautogui.locateAllOnScreen('data/checkbox.png')))
try:
    pyautogui.click('data/checkbox.png')
except:
    print('Image could not be found')
