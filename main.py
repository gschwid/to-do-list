from tkinter import *

# Creates the window
root = Tk()
root.title("Grant's task manager")

# Sets up user input for creating tasks
e = Entry(root,width= 50)
e.grid(row= 0,column= 0)
e.insert(0, "Enter your tasks: ")

# Creates button next to the input taker.
myButton = Button(background="black")
myButton.grid(row = 0, column=1)

# Creates the main window and continously runs.
root.mainloop()