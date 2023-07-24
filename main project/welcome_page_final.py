from tkinter import*
from PIL import ImageTk, Image

from tkinter import messagebox
welcome_window = Tk()
welcome_window.geometry('990x660+50+50')
welcome_window.resizable(0, 0)
welcome_window.title('Welcome Page')

def login():
    welcome_window.destroy()
    import user_login_final
def create():
    welcome_window.destroy()
    import create_final

#background Image
bg_image = Image.open('coins-glass-jar-money-saving-financial-concept.jpg')
bg_image = bg_image.resize((990, 660), Image.ANTIALIAS)
background = ImageTk.PhotoImage(bg_image)
background_label = Label(welcome_window, image=background)
background_label.place(x=0, y=0)



def login_page():
    welcome_window.destroy()
    import user_login_final

#frame for personal details
frame=Label(welcome_window,width=70,height=10,bg="white")
frame.place(x=50,y=350)

#Heading
heading=Label(text='Welcome To CACHE ',fg='#12AD2B',bg='white',font=("#12AD2B",30,"bold"))
heading.place(x=260,y=5)
heading=Label(text='Start your saving journey with us. ',fg='#12AD2B',bg='white',font=("brown",15,"bold"))
heading.place(x=290,y=70)


#Heading inside frame
heading=Label(frame,text='Please login to continue.\nIf you do not have an account click sign up button ',fg='#12AD2B',bg='white',font="bold")
heading.place(x=10,y=5)

# Login Button
login_button = Button(frame,text='Login', font=('Arial', 20, 'bold'), fg='white', bg='#12AD2B',
                      cursor='hand2', activebackground='red', activeforeground='white',command=login)
login_button.place(x=50,y=100)

# Create New Account Button
create_account_button = Button(frame, text='Sign up', font=('Arial', 20, 'bold'), fg='white',
                               bg='#12AD2B', activeforeground='white', activebackground='red', bd=0,
                               cursor='hand2',command=create)
create_account_button.place(x=250,y=100)



welcome_window.mainloop()
