from tkinter import *

# Keeps track of which row to add tasks to.
rowCount = 1

# Creates the window
root = Tk()
root.title("Grant's task manager")

# Function that button calls to add tasks to the window.
def createTasks():
    global rowCount
    task = e.get()
    myLabel = Label(text=task)
    myLabel.grid(row=rowCount, column=0)
    rowCount += 1 
    

# Sets up user input for creating tasks
e = Entry(root,width= 50)
e.grid(row= 0,column= 0)
e.insert(0, "Enter your tasks: ")

# Creates button next to the input taker.
myButton = Button(background="black",command=createTasks)
myButton.grid(row = 0, column=1)

# Creates the main window and continously runs.
root.mainloop()