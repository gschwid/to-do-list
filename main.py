from tkinter import *

# Keeps track of which row to add tasks to.
rowCount = 1

# Creates the window
root = Tk()
root.title("Grant's task manager")

# Function that button calls to add tasks to the window.
def createTasks():
    global rowCount
    allTheTasks = {} # For storing each of the tasks
    task = e.get()
    if len(task) != 0 and task != "Enter your tasks: ":
        myTask = Label(text=task) 
        myTask.grid(row=rowCount, column=0) # Adding task to the to-do-list
        taskButton = Button(background="black", command=lambda: removeTask(allTheTasks,taskButton))
        taskButton.grid(row=rowCount, column=1) # Adding button to the to-do-list that will remove the task
        allTheTasks[taskButton] = myTask # Adds the task to the dictionary, allowing it to be deleted later.
        clear(e) # Clears what the user inputs as a task.
        rowCount += 1 

# Function that removes task and button next to it. 
def removeTask(tasks,button : Button):
    global rowCount
    task:Label= tasks.get(button) # Accesses the needed task
    task.destroy()
    button.destroy()

# Clears what is in the entry bar
def clear(entry:Entry):
    entry.delete(0,len(entry.get())) # First param is start, second is end.  
    
# Sets up user input for creating tasks
e = Entry(root,width= 50)
e.grid(row= 0,column= 0)
e.insert(0, "Enter your tasks: ")

# Creates button next to the input taker.
inputButton = Button(background="black",command=createTasks)
inputButton.grid(row = 0, column=1)

# Creates the main window and continously runs.
root.mainloop()