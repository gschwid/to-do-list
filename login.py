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
    

# Creates the create account window.
def createAccount():
    createAccountPage = Toplevel()
    createAccountPage.title("Create Account")
    usernameLabel = Label(createAccountPage, text="Username  ").grid(row = 0, column=0)
    usernameInput = Entry(createAccountPage,width=20).grid(row = 0, column=1)
    PasswordLabel = Label(createAccountPage, text="Password  ").grid(row = 1, column=0)
    PasswordInput = Entry(createAccountPage,width=20).grid(row = 1, column=1)

new_user = Button(text="New user", command= createAccount)
new_user.pack()
returning_user = Button(text = "Returning user", command= login)
returning_user.pack()
mainloop()