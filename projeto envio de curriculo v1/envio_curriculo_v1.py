#o codigo escrito a baixo vai automatiza o envio de um currilo em um site espeficio.
import pyautogui
from time import sleep
pyautogui.moveTo(340,745,duration=1)
pyautogui.click(button='left')
pyautogui.moveTo(164,50,duration=1)
pyautogui.write('https://www.postosdallas.com/')
pyautogui.press('enter')
sleep(10)
pyautogui.moveTo(821,147,duration=1)
sleep(3)
pyautogui.click()
pyautogui.moveTo(786,178,duration=1)
pyautogui.click()
pyautogui.moveTo(1172,341,duration=1)
pyautogui.click(duration=1)
pyautogui.moveTo(591,307)
pyautogui.click()
pyautogui.write('Patricia oliveira da silva')
#escreve o nome no campo nome
sleep(2)
pyautogui.moveTo(514,382,duration=1)
#se move para o campo telefone
pyautogui.click()
pyautogui.write('91984742562')
pyautogui.press('esc')#cancela janelas inuteis no formulario
pyautogui.moveTo(758,393,duration=1)#move até o campo onde fica os bairros onde a pessoa mora
pyautogui.click(duration=1)
pyautogui.moveTo(754,348,duration=1)#se move ate o bairro
sleep(1)#da um pause para poder ficar em cima do bairro
pyautogui.moveTo(911,353,duration=1)
for i in range(10):
    pyautogui.click(duration=0)
pyautogui.moveTo(764,330,duration=1)
pyautogui.click()
pyautogui.moveTo(503,493,duration=1)
pyautogui.click()
pyautogui.write('patriciaoliveira8891@gmail.com')
pyautogui.press('esc')
pyautogui.moveTo(663,561,duration=1)#move-se até o botão para anexar o pdf
pyautogui.click()#clica no pdf
pyautogui.moveTo(367,55,duration=1)
pyautogui.click()
pyautogui.write('D:\curriculo patricia')#pesquisa o pdf dentro da pasta 
pyautogui.moveTo(429,56,duration=1)#se move ate o local do pfd
pyautogui.click()#clica no pdf
pyautogui.moveTo(421,162,duration=1)#se move ate o botao abrir da janela
pyautogui.click()#clica no botão abrir
pyautogui.moveTo(512,443,duration=1)#
pyautogui.click()#
pyautogui.moveTo(514,643,duration=2)#vai ate a caixa de dialogo
pyautogui.click()#clica confirmando que mora nas proximidades
pyautogui.scroll(-100)#rola ate o botão enviar
pyautogui.moveTo(620,658,duration=1)#se move ate o botão enviar 
#pyautogui.click()#clica no botão enviar 
