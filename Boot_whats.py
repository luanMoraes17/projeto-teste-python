import webbrowser
import pyautogui
from time import sleep


telefones = [55112222222]

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(5)
    pyautogui.click(559,263,duration=1)
    sleep(5)
    pyautogui.typewrite('Gostaria de participar do nosso evento?(digite sim, se gostaria de participar.')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)