#init
from tkinter import *

window = Tk()
window.geometry("900x900")
window.title("To-Do List")
window.resizable(False, False)
notes = Listbox(window)


#Functions
def get_box():
    retrieve = ENTRY_BOX.get("1.0", "end-1c")
    ENTRY_BOX.delete("1.0", "end-1c") 
    
    i = 0
    f = open("Notes_tkinter.txt", "a+")
    
    f.write(str(retrieve) + "\n")
    f.close()
    notes.insert(1 + i, retrieve)
    i += 1
def show_notes( ):
    notes.pack() 
def delete():
    db = notes.curselection()

    db = int(db[0])
    notes.delete(db )
def hide_notes(): 
    notes.pack_forget()
def openNewWindow():

     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("All Sessions Notes")
 
    # sets the geometry of toplevel
    newWindow.geometry("700x700")
 
    # A Label widget to show in toplevel
    f= open("Notes_tkinter.txt", "r")
    Label(newWindow,
          text =str(f.read())).pack()
    f.close()
#Files
DELETE_IMG = PhotoImage(file='/Users/zaidr/Downloads/delete.png')
#Components
delete = Button(window, text="Delete", command=delete, image=DELETE_IMG, borderwidth=0)
delete.pack(pady=10)
hide = Button(window, command=hide_notes, text="Hide Notes", font="Times")
ENTRY_BOX = Text(window, height="3", width="35", font="Times")
ADD_NOTE = Button(window, command=get_box, text="Add Note", font="Times")  
show_notes = Button(window, command=show_notes, text="Show Notes", font="Times")
show_all = Button(window, text="Show All Notes", command=openNewWindow, font="Times")
#Pack
show_all.pack()
ENTRY_BOX.pack()
ADD_NOTE.pack()
show_notes.pack()
hide.pack()


#Mainloop
window.mainloop()