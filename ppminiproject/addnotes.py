#Pin Your Note
#Import Necessary modules
import sqlite3 as sql
from tkinter import *
from tkinter import messagebox
# Create database connection and connect to table
try:
       con = sql.connect('pin_your_note.db')
       cur = con.cursor()
       cur.execute('''CREATE TABLE notes_table
                        (date text, notes_title text, notes text)''')
except:
       print("Connected to table of database")


def select_date():
    # Create Object
    root = Tk()

    # Set geometry
    root.geometry("400x400")

    # Add Calendar
    cal = Calendar(root, selectmode='day',
                    year=2020, month=5,
                    day=22)

    cal.pack(pady=20)

    def grad_date():
        date.config(text="Selected Date is: " + cal.get_date())
        root.destroy()

    def close():
        root.destroy()
        # root.quit()

 # Add Button and Label
Button(root, text="Get Date",
    command=grad_date).pack(pady=30)

date = Label(window, text="")
date.pack(pady=20)

'''notes_title_label = Label(window, text="Notes title:").place(x=10,y=50)

Button(root, text= "Close the Window", font=("Calibri",14,"bold"), command=close).pack(pady=20)'''

# Execute Tkinter
root.mainloop()


def add_notes():
       #Get input values
       today = date_entry.get()
       notes_title = notes_title_entry.get()
       notes = notes_entry.get("1.0", "end-1c")
       #Raise a prompt for missing values
       if (len(today) <=0) & (len(notes_title)<=0) & (len(notes)<=1):
               messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
       else:
       #Insert into the table
               cur.execute("INSERT INTO notes_table VALUES ('%s','%s','%s')" %(today, notes_title, notes))
               messagebox.showinfo(message="Note added")
       #Commit to preserve the changes
               con.commit()
