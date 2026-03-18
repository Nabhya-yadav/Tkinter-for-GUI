from tkinter import*

window=Tk()
window.geometry("400x300")
def Topwindow():
    window1=Toplevel()
    window1.geometry("100x200")
    label1=Label(window1,text="This is Toplevel")
    label1.pack()
    window1.mainloop()

label=Label(window,text="This is a main window")
label.pack()

button=Button(window,text="Click to open another window" ,command=Topwindow)
button.pack()



window.mainloop()