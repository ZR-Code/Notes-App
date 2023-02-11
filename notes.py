#init
from tkinter import *
from PIL import Image, ImageTk
import time

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

    date_question = Toplevel(window)
    date_question.title("Due Date")
    date_question.geometry("100x100")
    date_question.resizable(False, False)
    y_text = Label(date_question, text="y", font="Times").place(x=20, y=30)
    m_text = Label(date_question, text="m", font="Times").place(x=43, y=30)
    d_text = Label(date_question, text="d", font="Times").place(x=70, y=30)
    YEAR = Text(date_question, height="1", width="4", font="Times").place(x=10, y=50)
    MONTH = Text(date_question, height="1", width="2", font="Times").place(x=40, y=50)
    DAY = Text(date_question, height="1", width="2", font="times").place(x=65,y=50)
    def submit():
        pass
    submit_note = Button(date_question, text="Submit Date", font="Times", command=submit)
def show_notes( ):
    notes.place(x=107, y=150)
def fater():
    db = notes.curselection()
    results = ''
    for i in db:
        results = '\u0336'.join(notes.get(i)) + '\u0336'

    print(results)
 

    db = int(db[0])
    notes.delete(db)
    notes.insert(1, results)
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
def del_img():
    dc = notes.curselection()
    dc = int(dc[0])
    notes.delete(dc)
#Files
# Show Image
show_img = Image.open('/Users/zaidr/Desktop/Coding/Notes-App/Images/show.png')
show_img = show_img.resize((35, 35))
SHOW_IMG = ImageTk.PhotoImage(show_img)
# Hide Image
hide_img = Image.open('/Users/zaidr/Desktop/Coding/Notes-App/Images/hide.png')
hide_img = hide_img.resize((35, 35))
HIDE_IMG = ImageTk.PhotoImage(hide_img)
# Add Image
add_img = Image.open('/Users/zaidr/Desktop/Coding/Notes-App/Images/plus.png')
add_img = add_img.resize((35, 35))
ADD_IMG = ImageTk.PhotoImage(add_img)
# Mark Image
mark = Image.open('/Users/zaidr/Desktop/Coding/Notes-App/Images/right.png')
mark = mark.resize((35, 35))
MARK_IMG = ImageTk.PhotoImage(mark)
# Delete Image
delete = Image.open('/Users/zaidr/Desktop/Coding/Notes-App/Images/del.png')
delete = delete.resize((35, 35))
DELETE_IMG = ImageTk.PhotoImage(delete)
#Components

delete_img = Button(window, text="del", command=del_img, image=DELETE_IMG)
mark = Button(window, text="Delete", command=fater, image=MARK_IMG)
hide = Button(window, command=hide_notes, text="Hide Notes", font="Times", image=HIDE_IMG)
ENTRY_BOX = Text(window, height="3", width="35", font="Times")
ADD_NOTE = Button(window, command=get_box, text="Add Note", font="Times", image=ADD_IMG)  
show_notes = Button(window, command=show_notes, text="Show Notes", font="Times", image=SHOW_IMG)
show_all = Button(window, text="Show All Notes", command=openNewWindow, font="Times")
#Pack
show_all.pack(pady=6)
ENTRY_BOX.pack()
ADD_NOTE.place(x=75, y= 100)
show_notes.place(x=125, y=100)
hide.place(x=175, y=100)
mark.place(x=225, y=100)
delete_img.place(x=275, y=100)



#Mainloop
window.mainloop()