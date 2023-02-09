#init
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("400x400")
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
    notes.place(x=107, y=150)
def delete():
    db = notes.curselection()

    db = int(db[0])
    notes.delete(db )
def hide_notes(): 
    notes.place_forget()
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
# Show Image
show_img = Image.open('/Users/zaidr/Downloads/show.png')
show_img = show_img.resize((35, 35))
SHOW_IMG = ImageTk.PhotoImage(show_img)
# Hide Image
hide_img = Image.open('/Users/zaidr/Downloads/hide.png')
hide_img = hide_img.resize((35, 35))
HIDE_IMG = ImageTk.PhotoImage(hide_img)
# Add Image
add_img = Image.open('/Users/zaidr/Downloads/plus.png')
add_img = add_img.resize((35, 35))
ADD_IMG = ImageTk.PhotoImage(add_img)
# Delete Image
delete_img = Image.open('/Users/zaidr/Downloads/del.png')
delete_img = delete_img.resize((35, 35))
DELETE_IMG = ImageTk.PhotoImage(delete_img)
#Components
delete = Button(window, text="Delete", command=delete, image=DELETE_IMG, borderwidth=0)
hide = Button(window, command=hide_notes, text="Hide Notes", font="Times", image=HIDE_IMG, borderwidth=0)
ENTRY_BOX = Text(window, height="3", width="35", font="Times")
ADD_NOTE = Button(window, command=get_box, text="Add Note", font="Times", image=ADD_IMG)  
show_notes = Button(window, command=show_notes, text="Show Notes", font="Times", image=SHOW_IMG)
show_all = Button(window, text="Show All Notes", command=openNewWindow, font="Times")
#Pack
show_all.pack(pady=5)
ENTRY_BOX.pack()
ADD_NOTE.place(x=100, y= 100)
show_notes.place(x=150, y=100)
hide.place(x=200, y=100)
delete.place(x=250, y=100)



#Mainloop
window.mainloop()