from tkinter import*
window=Tk()
def click(event):
    print("\nButton is clicked")

button=Button(text="Click here")
button.pack()

button.bind("<Button-1>", click)

window.mainloop()