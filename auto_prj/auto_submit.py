import pyautogui
import time

# pyautogui.PAUSE = 0.3

# 노트패드 활성화
notepad = pyautogui.getWindowsWithTitle('notepad++')

if (len(notepad) > 0):
    print('notepad 찾았음')
    notepad_window = notepad[0]
    notepad_window.activate()  # notepad 활성화
    time.sleep(0.3)
    notepad_window.maximize()  # notepad 창 최대화

    pyautogui.hotkey('ctrl', 'a')  # 텍스트 전체 선택
    pyautogui.hotkey('ctrl', 'c')  # 텍스트 복사

    time.sleep(0.5)

    webpage = pyautogui.getWindowsWithTitle('chrome')
    if len(webpage) > 0:
        print('웹 페이지 찾았음')
        webpage_window = webpage[0]
        webpage_window.activate()  # 브라우저 활성화
        time.sleep(0.3)
        webpage_window.maximize()
        time.sleep(0.2)
        pyautogui.hotkey('alt', 'd')  # 주소란 포커스 이동
        pyautogui.write('https://apps.crossref.org/SimpleTextQuery')
        pyautogui.write(['enter'])
        time.sleep(2)
        pyautogui.write(['\t', '\t', '\t', '\t', '\t',])  # tab 5번 누르고
        pyautogui.hotkey('ctrl', 'v')  # 복사된 텍스트 붙여놓기
        time.sleep(0.2)
        pyautogui.write(['\t', ' '])  # 첫번째 체크박스 체크
        time.sleep(0.2)
        pyautogui.write(['\t', ' '])  # 두번째 체크박스 체크
        time.sleep(0.2)
        pyautogui.write(['\t', 'enter'])  # Submit버튼 클릭
