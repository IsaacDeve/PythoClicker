import keyboard
import mouse
import time
from colorama import init, Fore
init()

def changeWorkState():
    global clicker_on
    clicker_on = not clicker_on

print(Fore.GREEN + "\n---------PYTHOCLICKER---------")

buttonClick = str(input(Fore.GREEN + "\nLeft, middle, or right click?: " + Fore.RESET))
clickSpeed = float(input(Fore.GREEN + "\nSpeed (in seconds): " + Fore.RESET))
buttonStart = str(input(Fore.GREEN + "\nButton to activate with: " + Fore.RESET))
doLockMouse = str(input(Fore.GREEN + "\nLock mouse on certain coordinates? y/n: " + Fore.RESET).lower())

doLockMouseBool = False

lockMouseX = 1920/2 #960
lockMouseY = 1080/2 #540

if doLockMouse == "y":
    doLockMouseBool = True
    lockMouseX = int(input(Fore.GREEN + "\n        X: " + Fore.RESET))
    lockMouseY = int(input(Fore.GREEN + "\n        Y: " + Fore.RESET))

print(Fore.GREEN + "\n---------PYTHOCLICKER---------")

clicker_on = False
keyboard.add_hotkey(str(buttonStart).lower(), changeWorkState)

while True:
    if clicker_on:
        if doLockMouseBool:
            mouse.move(lockMouseX, lockMouseY)
        mouse.click(button=buttonClick.lower())
        time.sleep(clickSpeed)