from tkinter import *

# Creates the window
root = Tk()
root.title("Returning or new?")

# Creates the login window.
def login():
    loginPage = Toplevel()
    loginPage.title("Login")
    usernameLabel = Label(loginPage, text="Username  ").grid(row = 0, column=0)
    usernameInput = Entry(loginPage,width=20).grid(row = 0, column=1)
    PasswordLabel = Label(loginPage, text="Password  ").grid(row = 1, column=0)
    PasswordInput = Entry(loginPage,width=20).grid(row = 1, column=1)

def createFile(username, password):
    if username == "" or password == "":
        return # Makes it so user input has to exist.
    else:
        f = open(username + ".csv", "w")
        f.write(password+",")
        f.close()
        root.destroy()
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
    makeAccount = Button(createAccountPage,text="Done", command=lambda: createFile(usernameInput.get(),passwordInput.get())).grid(row=2,column=0)

# Buttons on main screen to determine if the user wants to create an account, or login to one. 
new_user = Button(text="New user", command= createAccount)
new_user.pack()
returning_user = Button(text = "Returning user", command= login)
returning_user.pack()

mainloop()