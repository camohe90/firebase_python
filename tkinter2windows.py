from tkinter import *


def createNewWindow():
    newWindow = Toplevel(app)
    labelExample = Label(newWindow, text = "New Window")
    buttonExample = Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

app = Tk()
buttonExample = Button(app, 
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()