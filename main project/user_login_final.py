from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkcalendar import Calendar
import pymysql

def login_user():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        if username_entry.get() == 'admin' and password_entry.get() == 'admin':
            messagebox.showinfo('Welcome', 'Login Successful')
            import dashboard
        else:
            messagebox.showerror('Error', 'Invalid Username or Password')

def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show='')
        show_password_button.config(image=hide_img)
    else:
        password_entry.config(show='*')
        show_password_button.config(image=show_img)

def signup_page():
    login_window.destroy()

def forget_pass():
    # Functionality for the forget password option
    messagebox.showinfo('Forgot Password', 'This feature is under development.')

def show_calendar():
    def get_date():
        selected_date = cal.get_date()
        date_label.config(text="Selected Date: " + selected_date)
        top.destroy()

    top = Toplevel(login_window)
    top.title("Calendar")

    cal = Calendar(top, selectmode="day")
    cal.pack(pady=10)

    select_button = Button(top, text="Select Date", command=get_date)
    select_button.pack(pady=5)

    date_label = Label(top, text="")
    date_label.pack(pady=5)

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
heading_label.grid(row=0, column=0, columnspan=2, pady=20)

# Username Entry
username_entry = Entry(login_frame, font=('Arial', 20), bd=0, highlightbackground='firebrick1')
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', lambda event: username_entry.delete(0, END))
username_entry.grid(row=1, column=0, columnspan=2, ipadx=10, pady=10)

# Password Entry
password_entry = Entry(login_frame, font=('Arial', 20), bd=0, show='*', highlightbackground='firebrick1')
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', lambda event: password_entry.delete(0, END))
password_entry.grid(row=2, column=0, ipadx=10, pady=10, padx=5)

# Show/Hide Password Button
show_img = ImageTk.PhotoImage(Image.open("show.jpg").resize((25, 25), Image.ANTIALIAS))
hide_img = ImageTk.PhotoImage(Image.open("hide.jpg").resize((25, 25), Image.ANTIALIAS))
show_password_var = BooleanVar()
show_password_button = Checkbutton(login_frame, text="Show Password", font=('Arial', 12),
                                        variable=show_password_var, onvalue=True, offvalue=False,
                                        command=toggle_password_visibility,
                                        indicatoron=False, padx=0, pady=0)
show_password_button.config(image=show_img, selectimage=hide_img)
show_password_button.grid(row=2, column=1, padx=5)

# Login Button
login_button = Button(login_frame, text='Login', font=('Arial', 20, 'bold'), fg='white', bg='#12AD2B',
                      activeforeground='white', activebackground='firebrick1', bd=0, width=20, command=login_user)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Forgot Password Label
forgot_password_label = Label(login_frame, text="Forgot Password?", font=('Arial', 15,'underline'), fg='blue', bg='white',
                              cursor='hand2')
forgot_password_label.grid(row=4, column=0, columnspan=2)
forgot_password_label.bind("<Button-1>", lambda event: forget_pass())

# Create New Account Label
create_account_label = Label(login_frame, text="Don't have an account?", font=('Arial', 15), fg='#12AD2B',
                             bg='white')
create_account_label.grid(row=5, column=0, columnspan=2)

# Create New Account Button
create_account_button = Button(login_frame, text='Create New One', font=('Arial', 15, 'underline'), fg='blue',
                               bg='white', activeforeground='blue', activebackground='white', bd=0,
                               cursor='hand2', command=signup_page)
create_account_button.grid(row=6, column=0, columnspan=2, pady=5)

# Open Calendar Button
calendar_button = Button(login_frame, text="Open Calendar", command=show_calendar)
calendar_button.grid(row=7, column=0, columnspan=2, pady=10)

login_window.mainloop()