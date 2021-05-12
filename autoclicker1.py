import pyautogui
import time 
xtarget = None
ytarget = None
time.sleep(3)
p = pyautogui.position() 
print(p)
xtarget = p.x
ytarget = p.y

mode = input("Enter speed (very fast, fast, medium, or slow):")

if mode == "fast":
    speed = 0.1 
elif mode == "medium":
    speed = 1
elif mode == "slow":
    speed = 2

while (True):
    pyautogui.click(xtarget, ytarget)
    
    if mode != "very fast":
        time.sleep(speed)