import pyautogui

wh = pyautogui.size()  # Obtain the screen resolution
print(f'wh: {wh}')

print(f'width: {wh[0]}, height: {wh[1]}')
print(f'width: {wh.width}, height: {wh.height}')

# absolute position
# for i in range(10):  # Move mouse in a square.
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# relative position
# for i in range(10):
#     pyautogui.move(100, 0, duration=0.25)
#     pyautogui.move(0, 100, duration=0.25)
#     pyautogui.move(-100, 0, duration=0.25)
#     pyautogui.move(0, -100, duration=0.25)

# Getting the Mouse Position
p = pyautogui.position()
print(f'Mouse position: {p}')
print(f'p.x: {p[0]}, p.y: {p[1]}')
print(f'p.x: {p.x}, p.y: {p.y}')
