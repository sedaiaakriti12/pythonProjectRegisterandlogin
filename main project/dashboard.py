from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time

dash = Tk()
dash.resizable(False, False)
dash.geometry('990x660+50+50')

frame_1=LabelFrame(dash, width = 250, height = 640, font = ('arial',20,'bold'),bg = '#c9df8a',bd = 15, relief = 'ridge')
frame_1.place(x=10,y=10)
frame_2=LabelFrame(dash, width = 725, height = 70, font = ('arial',20,'bold'),bg = 'white', relief = 'ridge')
frame_2.place(x=260,y=10)


heading1=Label(frame_2,text='Cache ',fg='#12AD2B',bg='white',font=("black",30,"bold"))
heading1.place(x=250,y=10)

Search=StringVar()
Entry(frame_2,textvariable=Search,width=15,bd=2,font='arial,20',bg='black').place(x=900,y=10)


dash.mainloop()