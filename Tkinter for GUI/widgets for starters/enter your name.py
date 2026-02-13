from tkinter import*
from datetime import date


screen=Tk()

screen.title("Demo screen")
screen.geometry("500x500")
label1=Label(text="Welcome", fg="blue",bg="white", height=1,width=100)
label2=Label(text="Enter your name", fg="white",bg="blue",)
entry=Entry()
def click():
    name=entry.get()
    global Message
    Message="Welcome to the Application! \nToday's date is: "
    greet="Hello "+name+"\n"
    textBox.insert(END,greet)
    textBox.insert(END,Message)
    textBox.insert(END,date.today())
    

textBox=Text(height=5)
btn=Button(text="submit", bg="orange",command=click)
label1.pack()
label2.pack()
entry.pack()
btn.pack()
textBox.pack()

screen.mainloop()