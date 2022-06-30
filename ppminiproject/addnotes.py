#Pin Your Note -TechVidvan
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
       # Insert a row of data
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