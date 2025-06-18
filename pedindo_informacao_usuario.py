'''crie um programa que pode o usario e senha e na 
sequencia,copie e cole o usuario e senha dentro de 
um bloco de notas'''
import pyautogui
import pyperclip
from time import sleep
pyautogui.hotkey('win','r')
sleep(1)
pyautogui.write('notepad',interval=0.1)
sleep(1)
pyautogui.press('enter')
sleep(1)
nome=pyautogui.prompt('Digite o seu usuario:',title='Dados de Login')
#senha=pyautogui.prompt('Digite a sua senha')
senha=pyautogui.password(text='Digite a sua senha',title='Dados de Login',mask='*')
def usuario(nome):
    pyperclip.copy(nome)
    pyautogui.write(nome,interval=0.1)
    pyautogui.press('enter')
usuario(nome)

def chave (senha):
    pyperclip.copy(senha)
    pyautogui.write(senha,interval=0.1)
chave (senha)




    





