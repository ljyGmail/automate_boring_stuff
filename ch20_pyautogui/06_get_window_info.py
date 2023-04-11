import pyautogui

# pyautogui.sleep(3)
# Obtaining the Active Window
active_win = pyautogui.getActiveWindow()
print(active_win)
print(f'left: {active_win.left}, right: {active_win.right}')
print(f'top: {active_win.top}, bottom: {active_win.bottom}')

print(f'topleft: {active_win.topleft}, topright: {active_win.topright}')
print(
    f'bottomleft: {active_win.bottomleft}, bottomright: {active_win.bottomright}')

print(f'midleft: {active_win.midleft}, midright: {active_win.midright}')
print(f'midtop: {active_win.midtop}, midbottom: {active_win.midbottom}')

print(f'width: {active_win.width}, height: {active_win.height}')
print(f'size: {active_win.size}')
print(f'area: {active_win.area}')

print(f'center: {active_win.center}')
print(f'centerx: {active_win.centerx}')
print(f'centery: {active_win.centery}')

print(f'box: {active_win.box}')

print(f'title: {active_win.title}')

# pyautogui.click(active_win.left+200, active_win.top+200)

# Other Ways of Obtaining Windows
print(f'all windows: {pyautogui.getAllWindows()}')
print(f'windows at: {pyautogui.getWindowsAt(200, 200)}')
print(
    f'windows with title: {pyautogui.getWindowsWithTitle("notepad++")}')
print(f'active window: {pyautogui.getActiveWindow()}')

# Manipulating Windows
print(active_win.isMaximized)
print(active_win.isMinimized)
print(active_win.isActive)
active_win.restore()
pyautogui.sleep(0.5)
active_win.width = 700
pyautogui.sleep(0.5)
active_win.topleft = (600, 400)
pyautogui.sleep(0.5)
active_win.minimize()
pyautogui.sleep(3)
active_win.restore()
pyautogui.sleep(2)
# active_win.close()
active_win.maximize()
