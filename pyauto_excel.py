import pyautogui as pg
import pyperclip
import datetime

pg.PAUSE=3
pg.press("win")
pyperclip.copy(r'c:\Users\User\test.xlsx')
pg.hotkey('ctrl','v')
pg.press('enter')
