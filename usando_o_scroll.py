import pyautogui
from time import sleep
pyautogui.moveTo(1191,30,duration=1)
pyautogui.click(button='left')
sleep(2)
pyautogui.write('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal')
sleep(1)
pyautogui.press('enter')
pyautogui.moveTo(956,180,duration=1)
pyautogui.scroll(-402)
pyautogui.moveTo(1080,190,duration=1)
pyautogui.click(button='left')
for i in range(20):
    sleep(2)
    pyautogui.scroll(-200)
pyautogui.moveTo(1157,34,duration=1)
pyautogui.click(button='left')

