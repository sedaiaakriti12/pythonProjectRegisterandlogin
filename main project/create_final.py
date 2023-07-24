import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk
from tkinter import ttk
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import os

signup_window = Tk()
signup_window.title('Signup Page')
signup_window.resizable(False, False)
signup_window.geometry('990x660+50+50')
signup_window.configure(bg='white')
bgLabel = Label(signup_window)
bgLabel.grid()


bg_image = Image.open('Abstract c letter logo template.png')
bg_image = bg_image.resize((200,200), Image.ANTIALIAS)
background = ImageTk.PhotoImage(bg_image)
background_label = Label(signup_window, image=background)
background_label.place(x=10, y=0)

frame_1 = LabelFrame(signup_window, width = 950, height = 390, font = ('arial',20,'bold'),bg = 'white',bd = 15, relief = 'ridge')
frame_1.place(x=15,y=250)
frame_2 = LabelFrame(frame_1, width = 900, height = 50, font = ('arial',10,'bold'), \
                                               bg = 'white', relief = 'ridge', bd = 13)
frame_2.place(x=300,y=270)


#Heading
heading1=Label(text='Create New Account ',fg='#12AD2B',bg='white',font=("black",30,"bold"))
heading1.place(x=350,y=5)

heading2 = Label(text='Please Fill Out The Form', font=('Microsoft Yahei UI Light', 20, 'bold'), bg='white',
                fg='#12AD2B')

heading2.place(x=350,y=200)



#for name
def on_enter(e):
    name.delete(0,'end')

def on_leave(e):
    name.get()
    if name=='':
        name.insert(0,'Name')

name = Entry(frame_1,width=20,fg='black',border=2,bg='white',font='arial')
name.place(x=1,y=2)
name.insert(0,'Name')
name.bind('<FocusIn>',on_enter)
name.bind('<FocusOut>',on_leave)

#for date of birth
def on_enter(e):
    date_of_birth.delete(0,'end')

def on_leave(e):
    date_of_birth.get()
    if date_of_birth=='':
        date_of_birth.insert(0,'Date Of Birth')


sel=StringVar() # declaring string variable
style = ttk.Style(signup_window)
style.theme_use('clam') #Theme to be changed # alt , classic, clam
style.configure('my.DateEntry',
                fieldbackground='white',
                background='white',
                foreground='dark blue',
                arrowcolor='red',
				)

date_of_birth = DateEntry(frame_1,style='my.DateEntry',width=30,fg='black',border=2,selectmode='day',textvariable=sel)
date_of_birth.place(x=300,y=2)
date_of_birth.insert(0,'Date Of Birth')
date_of_birth.bind('<FocusIn>',on_enter)
date_of_birth.bind('<FocusOut>',on_leave)


#for gender
def on_enter(e):
    gender.delete(0,'end')

def on_leave(e):
    gender.get()
    if gender=='':
        gender.insert(0,'Gender')
gender = Entry(frame_1,width=20,fg='black',border=2,bg='white',font='arial')
gender.place(x=600,y=2)
gender.insert(0,'Gender')
gender.bind('<FocusIn>',on_enter)
gender.bind('<FocusOut>',on_leave)

#for guardian name
def on_enter(e):
    guardian_name.delete(0,'end')

def on_leave(e):
    guardian_name.get()
    if guardian_name=='':
        guardian_name.insert(0,'Guardian Name')

guardian_name = Entry(frame_1,width=20,fg='black',border=2,bg='white',font='arial')
guardian_name.place(x=1,y=50)
guardian_name.insert(0,'Guardian Name')
guardian_name.bind('<FocusIn>',on_enter)
guardian_name.bind('<FocusOut>',on_leave)

#occupation
def on_enter(e):
    occupation.delete(0,'end')

def on_leave(e):
    occupation.get()
    if occupation=='':
        occupation.insert(0,'Occupation')
occupation = Entry(frame_1,width=20,fg='black',border=2,bg='white',font='arial')
occupation.place(x=300,y=50)
occupation.insert(0,'Occupation')
occupation.bind('<FocusIn>',on_enter)
occupation.bind('<FocusOut>',on_leave)

#citizenship number
def on_enter(e):
    Address.delete(0, 'end')

def on_leave(e):
    Address.get()
    if Address== '':
        Address.insert(0, 'Address')
Address= Entry(frame_1, width=20, fg='black', border=2, bg='white', font='arial')
Address.place(x=600, y=50)
Address.insert(0, 'Address')
Address.bind('<FocusIn>', on_enter)
Address.bind('<FocusOut>', on_leave)

#address
def on_enter(e):
    Email_address.delete(0,'end')

def on_leave(e):
    Email_address.get()
    if Email_address=='':
        gender.insert(0,'address')
Email_address= Entry(frame_1,width=20,fg='black',border=2,bg='white',font='arial')
Email_address.place(x=1,y=90)
Email_address.insert(0,'Email Address')
Email_address.bind('<FocusIn>',on_enter)
Email_address.bind('<FocusOut>',on_leave)

def on_enter(e):
    Username.delete(0,'end')

def on_leave(e):
    Username.get()
    if Username=='':
        Username.insert(0,'address')
Username= Entry(frame_1,width=20,fg='black',border=2,bg='white',font='arial')
Username.place(x=300,y=90)
Username.insert(0,'Username')
Username.bind('<FocusIn>',on_enter)
Username.bind('<FocusOut>',on_leave)

def on_enter(e):
    Password.delete(0,'end')

def on_leave(e):
    Password.get()
    if Password=='':
        Password.insert(0,'address')
Password= Entry(frame_1,width=20,fg='black',border=2,bg='white',font='arial')
Password.place(x=600,y=90)
Password.insert(0,'Password')
Password.bind('<FocusIn>',on_enter)
Password.bind('<FocusOut>',on_leave)


import tkinter as tk
from tkinter import ttk


#Citizenship_photo
heading1=Label(frame_1,text='Please Upload Your Citizenship Photo ',fg='black',bg='white',font=("black",15,'bold'))
heading1.place(x=1,y=150)
def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetype=(
    ("JPG File", ".jpg"), ("PNG file", ".png"), ("All file", "how are you.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

btnSave = Button(frame_2, text = 'CREATE', font = ('arial',10,'bold'), width = 8,bg='#12AD2B',fg='white' )
btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
btnUpdate = Button(frame_2, text = 'BACK', font = ('arial',10,'bold'), width = 8,bg='#12AD2B',fg='white')
btnUpdate.grid(row = 0, column = 3, padx = 10, pady = 10)
btnExit = Button(frame_2, text = 'EXIT', font = ('arial',10,'bold'), width = 8,bg='#12AD2B',fg='white')
btnExit.grid(row = 0, column = 6, padx = 10, pady = 10)

lbl=Label()



btn = Button(frame_1, text="Select Image", command=showimage)
btn.place(x=1,y=200)

signup_window.title("Image Viewer")



signup_window.mainloop()