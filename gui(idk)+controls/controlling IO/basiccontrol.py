import pyautogui
import time

def screensize():
    print(pyautogui.size())

def mousepos():
    return(pyautogui.position())
    #time.sleep(1)

def mousemove(x,y):
    pyautogui.moveTo(x,y, duration = 1)

def mousedrag_relative(x,y):
    pyautogui.dragRel(x,y, duration = 1)

def square():
    for i in range(5):
        pyautogui.dragRel(0, 100, duration = 1) 
        pyautogui.dragRel(100,0, duration = 1)
        pyautogui.dragRel(0, -100, duration = 1)
        pyautogui.dragRel(-100, 0, duration = 1)        
        
def scroll(a):
    pyautogui.scroll(a)

def clickpos(x,y):
    pyautogui.click(x,y) 

def typer():
    pyautogui.typewrite("hello Geeks !")
    pyautogui.typewrite(["a", "left", "ctrlleft"]) 

screensize()
print(mousepos())
#clickpos(52,222)
#mousemove(100,100)
#mousedrag_relative(50,50)
#square()
#scroll(200)
#typer()
