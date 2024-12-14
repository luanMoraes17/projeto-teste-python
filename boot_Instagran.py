# 1 - Navegar até o site https://www.instagram.com
import webbrowser
import pyautogui
from time import sleep

while True:
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(1)
    # 2 - Entrar com meu usuário
    pyautogui.click(327,360,duration=1)
    sleep(1)
    pyautogui.typewrite('xxxxxxx')
    sleep(1)
    # 3 - Entrar com a minha senha
    pyautogui.click(335,411,duration=1)
    sleep(1)
    pyautogui.typewrite('lxxxxxxx')
    sleep(1)
    # 4 - Clicar em "log in"
    pyautogui.click(448,473,duration=1)
    sleep(10)
    # 5 - Clicar em "Not now" para não salvar navegador
    pyautogui.click(464,692,duration=1)
    sleep(15)
    # 6 - fechar janela de "salvar senha"
  
    # 7 - Pesquisar pela pagina'
    pyautogui.click(521,139,duration=1)
    sleep(1)
    pyautogui.typewrite('nike')
    sleep(1)
    # 8 - Entrar na página
    pyautogui.move(0,65,duration=1)
    sleep(1)
    pyautogui.click()
    sleep(10)
    # 9 - Clicar na postagem mais recente
    pyautogui.click(165,905,duration=1)
    sleep(7)
    # 10 - Verificar se já curti ou não aquela postagem
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(1)
    # 11 - Se já tiver curtido, fazer nada, e pausar o bot por 24 horas
    if coracao is not None:
        sleep(86400)
    # 12 - Se não tiver curtido, curtir a foto
    elif coracao == None:
        pyautogui.click(312,858,duration=1)
        sleep(5)
        # 13 - Se não tiver curtido, comentar na foto
        pyautogui.click(381,838,duration=1)
        sleep(3)
        pyautogui.click(437,947,duration=1)
        sleep(1)
        pyautogui.typewrite('show!')
        sleep(5)
        pyautogui.click(651,944,duration=1)
        # 14 - Pausar por 24 horas
        sleep(86400)