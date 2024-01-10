from tkinter import *

rowCount = 1 # Variable to keep track of the amount of rows needed in the task manager.

# Creates the login window.
def login():
    loginPage = Toplevel()
    loginPage.title("Login")
    usernameLabel = Label(loginPage, text="Username  ").grid(row = 0, column=0)
    usernameInput = Entry(loginPage,width=20).grid(row = 0, column=1)
    PasswordLabel = Label(loginPage, text="Password  ").grid(row = 1, column=0)
    PasswordInput = Entry(loginPage,width=20).grid(row = 1, column=1)

# Creates the file to store data.
def createFile(username, password, win):
    if username == "" or password == "":
        return # Does nothing if either username or password is not input.
    else:
        f = open(username + ".csv", "w")
        f.write(password+",")
        f.close()
        win.destroy() # Closes the create account window.
        createTaskManager(username + ".csv", username)
        
# Creates the create account window.
def createAccount():
    createAccountPage = Toplevel()
    createAccountPage.title("Create Account")
    usernameLabel = Label(createAccountPage, text="Username  ").grid(row = 0, column=0)
    usernameInput = Entry(createAccountPage,width=20)
    usernameInput.grid(row = 0, column=1)
    passwordLabel = Label(createAccountPage, text="Password  ").grid(row = 1, column=0)
    passwordInput = Entry(createAccountPage,width=20)
    passwordInput.grid(row = 1, column=1)
    makeAccount = Button(createAccountPage,text="Done", command=lambda: createFile(usernameInput.get(),passwordInput.get(),createAccountPage)).grid(row=2,column=0)

# Function that button calls to add tasks to the window.
def createTasks(e : Entry,csvFile):
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
        f = open(csvFile, "a") # writes the new tasks into the csv file.
        f.write(task + ",")
        f.close()
        rowCount += 1  # updates row count for future tasks.

# Function that removes task and button next to it. 
def removeTask(tasks,button : Button):
    task:Label= tasks.get(button) # Accesses the needed task
    task.destroy()
    button.destroy()

# Clears what is in the entry bar
def clear(entry:Entry):
    entry.delete(0,len(entry.get())) # First param is start, second is end.  

# Initializes the task manager.
def createTaskManager(csvFile, name):
    root.title(name + "'s task manager")
    # Wipes the buttons originally on the root winodw.
    new_user.destroy()
    returning_user.destroy()
    # Sets up user input for creating tasks
    e = Entry(root,width= 50)
    e.grid(row= 0,column= 0)
    e.insert(0, "Enter your tasks: ")
    # Creates button next to the input taker.
    inputButton = Button(background="black",command=lambda: createTasks(e, csvFile))
    inputButton.grid(row = 0, column=1)

def main():
    # Bad coding practice to do this, with how I organized this its the easiest way for it to work.
    global root
    global new_user
    global returning_user
    # Creates the window
    root = Tk()
    root.title("Returning or new?")
    # Buttons on main screen to determine if the user wants to create an account, or login to one. 
    new_user = Button(text="New user", command= createAccount)
    new_user.pack()
    returning_user = Button(text = "Returning user", command= login)
    returning_user.pack()
    # Creates the main window and continously runs.
    mainloop()

if __name__ == "__main__":
    main()
