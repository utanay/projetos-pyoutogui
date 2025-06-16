'''crie um programa que vai ate onde seu bloco de notas 
estiver aberto e digite a frase AUTOMAÇÂO É INCRIVEL''' 
import pyautogui
import pyperclip # importa o interpretador de caracteres especiais
from time import sleep
pyautogui.hotkey('win','r')#chama o executar do windonws
pyautogui.write('notepad',interval=0.2)
pyautogui.press('enter')
sleep(2)
def frase_correta(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

frase_correta('A automação é incrivel')
pyautogui.moveTo(781,282,duration=1)
pyautogui.click(duration=1)