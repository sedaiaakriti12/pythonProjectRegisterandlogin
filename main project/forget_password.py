from tkinter import *
from PIL import ImageTk, Image
forget_pass=Tk()




forget_pass.geometry('400x505+50+50')

heading1=Label(text='Re-set Your Password',fg='#12AD2B',bg='white',font=("black",19,"bold"))
heading1.place(x=120,y=5)

bg_image = Image.open('Abstract c letter logo template.png')
bg_image = bg_image.resize((100,100), Image.ANTIALIAS)
background = ImageTk.PhotoImage(bg_image)
background_label = Label(forget_pass, image=background)
background_label.place(x=10, y=0)


frame_1 = LabelFrame(forget_pass, width = 355, height = 370,bg = 'white',bd = 15, relief = 'ridge')
frame_1.place(x=15,y=130)
forget_pass.configure(bg='white')
email_entry2 = Entry(frame_1, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry2.place(x=40, y=30, width=256, height=34)
email_entry2.config(highlightbackground="black", highlightcolor="black")
email_label2 = Label(frame_1, text='• Email account', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
email_label2.place(x=40, y=0)

    # ====  New Password ==================
new_password_entry = Entry(frame_1, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
new_password_entry.place(x=40, y=110, width=256, height=34)
new_password_entry.config(highlightbackground="black", highlightcolor="black")
new_password_label = Label(frame_1, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
new_password_label.place(x=40, y=80)

    # ====  Confirm Password ==================
confirm_password_entry = Entry(frame_1, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
confirm_password_entry.place(x=40, y=190, width=256, height=34)
confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
confirm_password_label = Label(frame_1, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                   font=("yu gothic ui", 11, 'bold'))
confirm_password_label.place(x=40, y=160)

    # ======= Update password Button ============
update_pass = Button(frame_1, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2')
update_pass.place(x=40, y=240, width=256, height=50)

forget_pass.mainloop()