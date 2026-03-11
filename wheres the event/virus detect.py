from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("200x200")
def message():
    messagebox.showwarning("ALERT", "virus DETECTED")

button=Button(window,text="Scan for virus", command=message)
button.place(x=40,y=80)



window.mainloop() 