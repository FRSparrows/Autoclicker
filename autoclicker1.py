import pyautogui
import time 
xtarget = None
ytarget = None
time.sleep(3)
p = pyautogui.position() 
print(p)
xtarget = p.x
ytarget = p.y

mode = input("Enter speed (fast, medium, or slow):")

if mode == "fast":
    speed = 0.1 
elif mode == "medium":
    speed = 1
elif mode == "slow":
    speed = 2
elif mode == "very fast":
    speed = 0.00000001
while (True):
    pyautogui.click(xtarget, ytarget)
    time.sleep(speed)
