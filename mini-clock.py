import time
import tkinter
from tkinter import ttk
def change():
    label['text']=time.asctime()
    root.after(1000,change)

root = tkinter.Tk()
big=ttk.Frame(root)
big.pack()

label=ttk.Label(big,text='0')
label.pack()

change()
root.wm_attributes("-topmost", True)
root.overrideredirect(True)
root.mainloop()
