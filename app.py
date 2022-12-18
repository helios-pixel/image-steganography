from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root=Tk()
root.title("Steganography")
root.geometry("700x515+150+180")
root.resizable(False,False)
root.configure(bg="#2f4155")


def showimage():
    # print("Show Image")
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",filetype=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image=img
    

def hide():
    # print("Data hidden")
    global secret
    message=t1.get(1.0, END)
    secret=lsb.hide(str(filename),message)

def show():
    # print("Data shown")
    clear_msg=lsb.reveal(filename)
    t1.delete(1.0,END)
    t1.insert(END, clear_msg)


def save():
    # print("Image Saved")
    secret.save("Stegano_Image.png")




#title_icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

#Logo
logo=PhotoImage(file="lbl.png")
Label(root, image=logo, bg="#2f4155").place(x=10,y=0)
Label(root, text="Image Steganography using LSB", bg="#2f4155",fg="white",font="Poppins 25 bold").place(x=100,y=20)

#frame1
f=Frame(root,bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10,y=80)
lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#frame2
f2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
f2.place(x=350,y=80)

t1=Text(f2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
t1.place(x=0,y=0,width=320, height=295)

sbar1=Scrollbar(f2)
sbar1.place(x=320,y=0, height=300)
sbar1.configure(command=t1.yview)
t1.configure(yscrollcommand=sbar1.set)

#frame3
f3=Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
f3.place(x=10,y=370)

Button(f3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=190,y=30)
Button(f3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=10,y=30)
Label(f3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

#frame4
f4=Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
f4.place(x=360,y=370)

Button(f4, text="Hide Data", width=10, height=2, font="arial 14 bold",command=hide).place(x=190,y=30)
Button(f4, text="Show Data", width=10, height=2, font="arial 14 bold", command=show).place(x=10,y=30)
Label(f4, text="Image Processes", bg="#2f4155", fg="yellow").place(x=20, y=5)

#frame5
f5=Frame(root, bd=3, bg="black", width=680, height=40, relief=GROOVE)
f5.place(x=10, y=470)
Label(f5, text="Developed by Pravin Tiwade (github.com/OREOwithWings)",bg="black",fg="white").place(x=0, y=5)

root.mainloop()