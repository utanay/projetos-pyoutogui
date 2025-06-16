'''crie um programa que vai ate onde seu bloco de notas 
estiver aberto e digite a frase AUTOMAÇÂO É INCRIVEL''' 
import pyautogui
import pyperclip # importa o interpretador de caracteres especiais
from time import sleep
pyautogui.hotkey('win','r')#chama o executar do windonws
pyautogui.write('notepad',interval=0.2)
pyautogui.press('enter')
sleep(2)
pyautogui.moveTo(492,632,duration=1)
pyautogui.click()
texto= input('Escreva algo no bloco de notas:')
#pyautogui.press('enter')
pyautogui.moveTo(701,751,duration=1)
pyautogui.click()
pyautogui.hotkey('ctrl','a')#seleciona tudo
sleep(1)
pyautogui.press('Backspace')
sleep(2)
def frase_correta(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl','v')

frase_correta(texto)
pyautogui.moveTo(781,282,duration=1)
pyautogui.click(duration=1)