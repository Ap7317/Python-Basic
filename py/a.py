import pyautogui
import time
time.sleep(4)
c=0
while c<=1000:
    pyautogui.typewrite("I like you"+str(c))
    pyautogui.press("enter")
    c=c+1