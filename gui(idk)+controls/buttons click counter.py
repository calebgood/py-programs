from tkinter import *


class A(Frame):
    

    def __init__(self, master):
        
        Frame.__init__(self, master)
        self.grid()
        self.count_var =0
        self.button()

    def button(self):
        
        self.button = Button(self)
        self.button["text"] = "Total Clicks: 0"
        self.button["command"] = self.count
        self.button.grid()

    def count(self):
        self.count_var += 1
        self.button["text"] = "Total Clicks: " + str(self.count_var)
        

root = Tk()
root.title("Buttons")
root.geometry("200x85")

x=A(root)

root.mainloop()
