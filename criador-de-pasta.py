#def criador_de_pastas():
import pyautogui
from time import sleep
for i in range (10):
     pyautogui.moveTo(210,387,duration=0)
     pyautogui.rightClick(x=210,y=387)
     sleep(0)
     pyautogui.moveTo(266,257,duration=0)
     sleep(0)
     pyautogui.click()
     pyautogui.moveTo(648,264,duration=0)
     pyautogui.click()
