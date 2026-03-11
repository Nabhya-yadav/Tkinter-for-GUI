from tkinter import*
window=Tk()
def keypressed(event):
    print(event.char)

window.bind("<Key>", keypressed)

window.mainloop()