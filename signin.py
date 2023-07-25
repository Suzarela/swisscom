from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def forget_pass():
    def change_password():
        if user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required', parent=window)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error', 'Password and Confirm are not matching', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='Sarafina26', database='userdata')
            mycurson = con.cursor()
            query = 'select * from data where username=%s'
            mycurson.execute(query, (user_entry.get()))
            row = mycurson.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycurson.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset, please log in with new password', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change password')

    background = ImageTk.PhotoImage(file='background_swisscom.png')
    bgLabel = Label(window, image=background)
    bgLabel.grid()

    frame = Frame(window, background='white', width=250, height=2)
    frame.place(x=400, y=100)

    heading_label = Label(frame, text='RESET PASSWORD', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white', fg='blue')
    heading_label.grid(row=0, column=0)

    user_Label = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
    user_Label.grid(row=1, column=0, sticky='w', padx=10, pady=(10, 0))

    user_entry = Entry(frame, width=28, font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
    user_entry.grid(row=2, column=0, sticky='w', padx=10)

    passwordLabel = Label(frame, text='New Password', font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
    passwordLabel.grid(row=3, column=0, sticky='w', padx=10, pady=(20, 0))

    newpass_entry = Entry(frame, width=28, font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
    newpass_entry.grid(row=4, column=0, sticky='w', padx=10)

    passwordLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
    passwordLabel.grid(row=5, column=0, sticky='w', padx=10, pady=(20, 0))

    confirmpass_entry = Entry(frame, width=28, font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
    confirmpass_entry.grid(row=6, column=0, sticky='w', padx=10)

    submitButton = Button(frame, text='Submit', font=('Open Sans', 12, 'bold'), bd=0, bg='blue', fg='white', activebackground='blue', activeforeground='white', width=15, command=change_password)
    submitButton.grid(row=7, column=0, pady=(20, 30))

    window.mainloop()

def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Sarafina26')
            mycurson = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established try again')
            return

        query = 'use userdata'
        mycurson.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycurson.execute(query, (usernameEntry.get(), passwordEntry.get()))

        row = mycurson.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Success', 'Login is successful')


def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='closeeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)
        

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

login_window = Tk()
login_window.geometry('680x545+50+50')
login_window.title('Login Page')
login_window.resizable(False, False)

background = ImageTk.PhotoImage(file='background_swisscom.png')
bgLabel = Label(login_window, image=background)
bgLabel.place(x=0, y=0)

frame = Frame(login_window, background='white')
frame.place(x=400, y=100)

heading = Label(frame, text='USER LOGIN', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white', fg='blue')
heading.grid(row=0, column=0)

usernameEntry = Entry(frame, width=28, font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
usernameEntry.grid(row=1, column=0, sticky='w', padx=20, pady=20)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

passwordEntry = Entry(frame, width=28, font=('Microsoft Yahei UI Light', 9, 'bold'), bg='white', fg='blue')
passwordEntry.grid(row=2, column=0, sticky='w', padx=20, pady=20)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=627, y=215)

forgetButton = Button(login_window, text='Forgot Password?', font=('Microsoft Yahei UI Light', 7, 'bold'), fg='blue', bd=0, bg='white', activebackground='white', cursor='hand2', activeforeground='grey', command=forget_pass)
forgetButton.place(x=558, y=235)

loginButton = Button(frame, text='Login', font=('Open Sans', 12, 'bold'), bd=0, bg='blue', fg='white', activebackground='blue', activeforeground='white', width=20, command=login_user)
loginButton.grid(row=3, column=0, pady=(15, 10))

orLabel = Label(frame, text='--------------- OR ---------------', font=('Open Sans', 10), fg='grey', bg='white')
orLabel.grid(row=4, column=0, pady=(0, 10))

facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bd=0, bg='white')
fbLabel.place(x=483, y=326)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bd=0, bg='white')
googleLabel.place(x=512, y=326)

twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bd=0, bg='white')
twitterLabel.place(x=555, y=326)
twitterLabel.place(x=555, y=326)

signupLabel = Label(frame, text="Don't have an account?", font=('Open Sans', 7, 'bold'), fg='black', bg='white')
signupLabel.grid(row=5, column=0, sticky='w', padx=20, pady=(30, 20))

newaccountButton = Button(login_window, text='Create New Account', font=('Open Sans', 7, 'bold underline'), bd=0, bg='white', fg='blue', activebackground='blue', activeforeground='white', command=signup_page)
newaccountButton.place(x=534, y=372)


login_window.mainloop()