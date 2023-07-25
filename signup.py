from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Sarafina26')
            mycurson = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issues. Please Try Again')
            return
        try:
            query = 'Create Database userdata'
            mycurson.execute(query)
            query = 'use userdata'
            mycurson.execute(query)
            query = 'Create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar (20))'
            mycurson.execute(query)
        except:
            mycurson.execute('use userdata')

        query = 'select * from data where username=%s'
        mycurson.execute(query, (usernameEntry.get()))

        row = mycurson.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already exists')

        else:
            query = 'insert into data(email,username,password) values (%s,%s,%s)'
            mycurson.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            import signin


def login_page():
    signup_window.destroy()
    import signin

signup_window = Tk()
signup_window.title('Signup Page')
signup_window.resizable(False, False)

background = ImageTk.PhotoImage(file='background_swisscom.png')
bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window, background='white')
frame.place(x=400, y=100)

heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white', fg='blue')
heading.grid(row=0, column=0)

emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
emailLabel.grid(row=1, column=0, sticky='w', padx=20, pady=(10, 0))

emailEntry = Entry(frame, width=28, font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
emailEntry.grid(row=2, column=0, sticky='w', padx=20)

usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
usernameLabel.grid(row=3, column=0, sticky='w', padx=20, pady=(10, 0))

usernameEntry = Entry(frame, width=28, font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
usernameEntry.grid(row=4, column=0, sticky='w', padx=20)

passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
passwordLabel.grid(row=5, column=0, sticky='w', padx=20, pady=(10, 0))

passwordEntry = Entry(frame, width=28, font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
passwordEntry.grid(row=6, column=0, sticky='w', padx=20)

confirmpasswordLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
confirmpasswordLabel.grid(row=7, column=0, sticky='w', padx=20, pady=(10, 0))

confirmpasswordEntry = Entry(frame, width=28, font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
confirmpasswordEntry.grid(row=8, column=0, sticky='w', padx=20)

check = IntVar()
termsandconditions = Checkbutton(frame, text='I agree to the Terms & Conditions', font=('Microsoft Yahei UI Light', 8, 'bold'), bg='white', cursor='hand2', variable=check)
termsandconditions.grid(row=9, column=0, sticky='w', padx=15, pady=10)

signupButton = Button(frame, text='Signup', font=('Open Sans', 12, 'bold'), bd=0, bg='blue', fg='white', activebackground='blue', activeforeground='white', width=15, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount = Label(frame, text="Don't have an account?", font=('Open Sans', 8, 'bold'), bg='white', fg='black')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=20, pady=10)

loginButton = Button(frame, text='Log in', font=('Open Sans', 8, 'bold underline'), bg='white', fg='blue', activeforeground='blue', activebackground='white', cursor='hand2', bd=0, command=login_page)
loginButton.place(x=150, y=353)

signup_window.mainloop()