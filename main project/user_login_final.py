from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql



def login_user():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234', database='userdata')
            cursor = con.cursor()
            query = 'SELECT * FROM data WHERE username=%s AND password=%s'
            cursor.execute(query, (username_entry.get(), password_entry.get()))
            row = cursor.fetchone()

            if row is None:
                messagebox.showerror('Error', 'Invalid Username or Password')
            else:
                messagebox.showinfo('Welcome', 'Login Successful')

            con.close()

        except Exception as e:
            messagebox.showerror('Error', f'Connection Error: {str(e)}')


def signup_page():
    login_window.destroy()


def forget_pass():
    # Functionality for the forget password option
    pass


login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0, 0)
login_window.title('Login Page')
welcome_label = Label(login_window, text='Welcome to Login Page', font=('Arial', 20, 'bold'), fg='firebrick1')
welcome_label.pack(pady=20)



# Background Image
bg_image = Image.open('coins-glass-jar-money-saving-financial-concept.jpg')
bg_image = bg_image.resize((990, 660), Image.ANTIALIAS)
background = ImageTk.PhotoImage(bg_image)
background_label = Label(login_window, image=background)
background_label.place(x=0, y=0)

# Login Frame
login_frame = Frame(login_window, bg='white', width=500, height=500)
login_frame.place(x=100, y=160)

# Heading
heading_label = Label(login_frame, text='USER LOGIN', font=('Arial', 25, 'bold'), fg='#12AD2B')
heading_label.pack(pady=20)

# Username Entry
username_entry = Entry(login_frame, font=('Arial', 20), bd=0, highlightbackground='firebrick1')
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', lambda event: username_entry.delete(0, END))
username_entry.pack(ipadx=10, pady=10)

# Password Entry
password_entry = Entry(login_frame, font=('Arial', 20), bd=0, show='*', highlightbackground='firebrick1')
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', lambda event: password_entry.delete(0, END))
password_entry.pack(ipadx=10, pady=10)

# Login Button
login_button = Button(login_frame, text='Login', font=('Arial', 20, 'bold'), fg='white', bg='#12AD2B',
                      activeforeground='white', activebackground='firebrick1', bd=0, width=20, command=login_user)
login_button.pack(pady=10)

# Forgot Password Label
forgot_password_label = Label(login_frame, text="Forgot Password?", font=('Arial', 15), fg='blue', bg='white',
                              cursor='hand2')
forgot_password_label.pack()

# Create New Account Label
create_account_label = Label(login_frame, text="Don't have an account?", font=('Arial', 15), fg='black',
                             bg='white')
create_account_label.pack()

# Create New Account Button
create_account_button = Button(login_frame, text='Create New One', font=('Arial', 15, 'underline'), fg='blue',
                               bg='white', activeforeground='blue', activebackground='white', bd=0,
                               cursor='hand2', command=signup_page)
create_account_button.pack(pady=5)


login_window.mainloop()
