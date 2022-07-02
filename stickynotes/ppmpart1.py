from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from tkinter import font 

no_of_windows = 1


class StickyNotes(Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.xclick = 0
        self.yclick = 0


        self.overrideredirect(True)
        global no_of_windows
        self.geometry('250x250+' + str(1000+no_of_windows*(-30)) + '+' + str(100 + no_of_windows*20))
        self.config(bg = '#838383')
        self.attributes('-topmost', 'true')
        self.resizable(True,True)

root = Tk()
root.withdraw()
sticky = StickyNotes(root) 
root.mainloop()