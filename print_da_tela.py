'''de um print do bloco de notas usando o print do pyautogui'''
#0 import o pyautogui e o Sleep
import pyautogui
from time import sleep
#1 abra o bloco de notas
pyautogui.hotkey('win','r')#Chama o executar do windonws
#2 escreva no campo do executar notepad
pyautogui.write('notepad',interval=0.1)#escreve no campo
#3 apertar enter
sleep(1) #da um atraso no processo de enter
pyautogui.press('enter')
pyautogui.moveTo(729,242,duration=1)#se move ate o bloco de notas 
pyautogui.click()
pyautogui.hotkey('ctrl','a')
pyautogui.press('bacbackspace')
sleep(1)
pyautogui.write('Estou no bloco de notas, ja pode tirar o Print',interval=0.1)
sleep(1)
#4 posicione o ponteiro do mouse ate uma extremidade para encontrar a localização
#pyautogui.moveTo(513,104,duration=1)
pyautogui.screenshot('bloco notas.jpg',region=(537,86,700,415))

