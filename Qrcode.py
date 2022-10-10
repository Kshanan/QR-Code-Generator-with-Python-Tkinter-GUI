import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import BOLD
from tkinter import END
import qrcode
import qrcode
import qrcode



root=tk.Tk()   
root.title("QR Code Generator")
root.geometry("600x400")

img=Image.open('./gb.jpg')     
img=img.resize((600,400),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)
bg_lbl=tk.Label(root,image=img_photo)  
bg_lbl.place(x=0,y=0,width=600,height=400)

def qrgen():
    try:
        img1= qrcode.make(txt_box.get())
        img1.save("qrcode.jpg")
        openimage()
    except:
        messagebox.showwarning(Warning,'Something Went Wrong')

def openimage():
    img1=Image.open('./qrcode.jpg')
    img1=img1.resize((200,200),Image.ANTIALIAS)
    img_photo=ImageTk.PhotoImage(img1)
    icon.delete('all')
    icon.create_image(0,0,anchor='nw',image=img_photo)
    icon.image=img_photo  

def clear():
    icon.delete('all')
    txt_box.delete(0,END)


heading_title=tk.Label(bg_lbl,text='Enter Content of the QR Code to be Generated',fg='black',bg='white',font=('times new roman',14,'bold'))
heading_title.place(x=70,y=14)

frame_one=tk.Frame(bg_lbl,highlightbackground='black',highlightthickness=2)
frame_one.place(x=40,y=50,width=500,height=40)

txt_box=tk.Entry(frame_one,font=('times new roman',22),width=60)
txt_box.grid(row=0,column=0,sticky='w')

btn1=tk.Button(root,text='Generate',font=('Times new roman',10,BOLD),bg='white',borderwidth=0,command=lambda:qrgen())
btn1.place(x=190,y=100,width=100,height=30)

btn2=tk.Button(root,text='Clear',font=('Times new roman',10,BOLD),bg='white',borderwidth=0,command=lambda:clear())
btn2.place(x=300,y=100,width=100,height=30)



frame_two=tk.Frame(bg_lbl,highlightbackground='black',highlightthickness=2)
frame_two.place(x=40,y=130,width=500,height=250)

icon=tk.Canvas(frame_two,bg='white',bd=0,highlightthickness=0)
icon.place(relx=0.30,rely=0.10,relwidth=0.4,relheight=0.8)





root.mainloop()