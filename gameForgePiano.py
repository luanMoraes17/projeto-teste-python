# quais são os passos manuais que devo transformar em código
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1401,510, duration=1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1263,420, (55, 139, 41)):
        click(1263,420)
    if pyautogui.pixelMatchesColor(1345,410, (55, 139, 41)):
        click(1345,410)
    if pyautogui.pixelMatchesColor(1451,415, (55, 139, 41)):
        click(1451,415)
    if pyautogui.pixelMatchesColor(1545,411, (55, 139, 41)):
        click(1545,411)