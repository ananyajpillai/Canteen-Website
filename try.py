from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox
import datetime as dt
import pyttsx3

no_of_windows = 1


class StickyNotes(Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.xclick = 0
        self.yclick = 0


        self.overrideredirect(True)
        global no_of_windows
        self.geometry('250x250+'+ str(1000+no_of_windows*(-30)) + '+' + str(100 + no_of_windows*20))
        self.config(bg = '#838383')
        self.attributes('-topmost', 'true')

        # titlebar
        self.titlebar = Frame(self, bg = '#F8F796', relief = 'flat', bd = 2)
        self.titlebar.bind('<Button-1>', self.get_pos)
        self.titlebar.bind('<B1-Motion>', self.move_window)
        self.titlebar.pack(fill = X, expand = 1, side = TOP)

        self.closebutton = Label(self.titlebar, text = 'X', bg = '#F8F7B6', relief = 'flat')
        self.closebutton.bind('<Button-1>', self.quit_window)
        self.closebutton.pack(side = RIGHT)

        self.newbutton = Label(self.titlebar, text = '+', bg = '#F8F7B6', relief = 'flat')
        self.newbutton.pack(side = LEFT)
        self.newbutton.bind('<Button-1>', self.another_window)

        date = dt.datetime.now()
        self.label = Label(self, text=f"{date:%A, %B %d, %Y}", font="Calibri, 10", bg='#FDFDCA')
        self.label.pack(fill = BOTH)
        
        self.speakbutton = Label(self.titlebar, text="Read", bg='#F8F7B6', relief='flat')
        self.speakbutton.bind('<Button-1>', self.speak)
        self.speakbutton.pack(side=RIGHT)
        
        self.savebutton = Label(self.titlebar, text="Save", bg='#F8F7B6', relief='flat')
        self.savebutton.bind('<Button-1>', self.save_text)
        self.savebutton.pack(side=LEFT)

        self.mainarea = tkst.ScrolledText(self, bg = '#FDFDCA', font=('Comic Sans MS', 14, 'italic'), relief = 'flat', padx = 5, pady = 10)
        self.mainarea.pack(fill = BOTH, expand = 1)
        
        self.listbutton = Label(self.titlebar, text="Listen", bg='#F8F7B6', relief='flat')
        self.listbutton.bind('<Button-1>', self.listen)
        self.listbutton.pack(side=RIGHT)

        self.shadow = Frame(self).pack(side=BOTTOM)
        self.shadow = Frame(self).pack(side=RIGHT)
        
        no_of_windows += 1
        
       
    def speak(self, event):
        engine = pyttsx3.init()
        engine.say(self.mainarea.get("1.0", END))
        print(self, event)
        engine.runAndWait()
        
    def listen(self, event):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.8
            r.energy_threshold = 200
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            print(self, event)
            self.mainarea.insert(END, query)

        except Exception:
            print("Please repeat...")
            return "None"
        return query
        
    def get_pos(self, event):
        self.xclick = event.x
        self.yclick = event.y

    def move_window(self, event):
        self.geometry('+{0}+{1}'.format(event.x_root-self.xclick, event.y_root-self.yclick))

    def another_window(self, event):
        sticky = StickyNotes(root)
        
    def save_text(self, event):
        try:
            text_file = open("test.txt", "a")
        except:
            text_file = open("test.txt", "w")
        print(self, event)
        text_file.write(str(self.mainarea.get('1.0', END)))
        text_file.close()

    def quit_window(self, event):
        self.closebutton.config(relief = 'flat', bd = 0)
        if(messagebox.askyesno('Delete Note?','Are you sure you want to delete this note?', parent = self)):
            global no_of_windows
            self.destroy()
            no_of_windows -= 1
            if(no_of_windows == 1):
                root.destroy()
            return
        self.closebutton.config(relief = 'flat', bd = 0, bg = '#F8F7B6')

root = Tk()
root.withdraw()
sticky = StickyNotes(root) 
root.mainloop()
