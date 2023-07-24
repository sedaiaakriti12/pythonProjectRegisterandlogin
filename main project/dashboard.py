from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from datetime import *
from tkinter import filedialog
import os
import time

dash = Tk()
dash.resizable(False, False)
dash.geometry('990x660+50+50')


def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select image file',
                                          filetype=(("JPG File", "*.jpg"),
                                                    ("PNG File", "*.png"),
                                                    ("All files", "*.txt")))
    image=(Image.open(filename))
    resize_image=image.resize((190,190))
    photo2=ImageTk.PhotoImage(resize_image)
    lbl.config(image=photo2)
    lbl.image=photo2


frame_1 = LabelFrame(dash, width=250, height=640, font=('arial', 20, 'bold'), bg='#c9df8a', bd=15, relief='ridge')
frame_1.place(x=10, y=10)
frame_2 = LabelFrame(dash, width=725, height=70, font=('arial', 20, 'bold'), bg='white', relief='ridge')
frame_2.place(x=260, y=10)

heading1 = Label(frame_2, text='Cache ', fg='#12AD2B', bg='white', font=("black", 30, "bold"))
heading1.place(x=250, y=10)

# image
image = PhotoImage(file='upload photo.png', height=190, width=190)
lbl = Label(frame_1, image=image)
lbl.place(x=10, y=0)

# button
Button(frame_1, text='Upload', width='15', height=1, font='arial 12 bold', fg='#12AD2B', bg='white',
       command=showimage).place(x=25, y=200)

dash.mainloop()
