import pyautogui

pyautogui.PAUSE=1.0

width,height = pyautogui.size()

pyautogui.moveTo(5,height-5,duration=1)
pyautogui.click()

pyautogui.write("memo")
pyautogui.press("enter")

pyautogui.write("It was created using the Python module pyautogui.")

pyautogui.hotkey("ctrl","s")

pyautogui.write("Python.txt",interval=0.25)
pyautogui.press("enter")
