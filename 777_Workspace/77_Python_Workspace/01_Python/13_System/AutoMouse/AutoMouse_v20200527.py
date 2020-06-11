import pyautogui
import time

print('hello world')
screenWidth, screenHeight = pyautogui.size()

pyautogui.moveTo(830, 410)
pyautogui.click(interval=0.5)
pyautogui.moveTo(830, 410)
pyautogui.click(interval=0.5)

for i in range(1, 10000):
    print(i, 'start')
    pyautogui.moveTo(830, 410)
    pyautogui.click()
    pyautogui.moveTo(830, 412)
    pyautogui.click()
    print(i, 'end')
    time.sleep(600)

