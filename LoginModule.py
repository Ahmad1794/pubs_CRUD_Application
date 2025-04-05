from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image,ImageTk

import pyodbc
from UserInterfaceLayer.MainModule import MainForm

loginForm = Tk()
loginForm.title('Login Form')
loginForm.geometry('420x240')
loginForm.iconbitmap('Images/login.ico')
loginForm.resizable(0, 0)
x = int(loginForm.winfo_screenwidth() // 2 - 420 // 2)
y = int(loginForm.winfo_screenheight() // 2 - 240 // 2)
loginForm.geometry('+{}+{}'.format(x, y))

image = Image.open('Images/bookstore1.png')
bg_image = ImageTk.PhotoImage(image)

label = Label(loginForm, image=bg_image)
label.place(x=0, y=0, relwidth=1, relheight=1)



def checkLogin():
    userName = txtUserName.get()
    password = txtPassword.get()
    connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=Ahmad_Ahmadi_DS140303_pythonProject;Trusted_Connection=yes"
    commandText = "execute [dbo].[LoginCheck] ?, ?"
    params = (userName, password)
    connection = pyodbc.connect(connectionString)
    cursor = connection.cursor()
    cursor.execute(commandText, params)
    rows = cursor.fetchall()
    if len(rows) > 0:
        fullName = rows[0][3] + ' ' + rows[0][4]
        loginForm.destroy()
        mainFormObject = MainForm()
        mainFormObject.mainFormLoad()

    else:
        msg.showerror('ERROR', "UserName or Password is incorrect!")
lblUserName = Label(loginForm, text='Username :')
lblUserName.grid(row=1, column=0, padx=10, pady=15,sticky=W)
txtUserName = StringVar()
entUserName = ttk.Entry(loginForm, width=15, textvariable=txtUserName)
entUserName.grid(row=2, column=0,padx=10,pady=0)
lblPassword = Label(loginForm, text='Password :')
lblPassword.grid(row=3, column=0, padx=10, pady=15,sticky=W)
txtPassword = StringVar()
entPassword = ttk.Entry(loginForm, width=15, textvariable=txtPassword,show='*')
entPassword.grid(row=4, column=0, padx=10)
loginFormImage = PhotoImage(file='Images/loginForm7.png')
loginbtn = ttk.Button(loginForm, text='Login', compound=TOP, command=checkLogin,width=14)
loginbtn.grid(row=5, column=0,padx=10,pady=30,sticky=W)

loginForm.mainloop()
