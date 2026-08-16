from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.title("Denomiation Conter")
root.columnconfigure(bg='light blue')
root.geometry('600x600')
upload=Image.open("app_image.jpg")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,bg='light blue')
label.place(x=180,y=20)
label1=Label(root,text='Hello welcome to denomination Coulater applicasion.',bg='light blue')
label1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    Msgbox=messagebox.showinfo("Alert","Do you want to caculate the demonination cont?")
    if Msgbox == 'ok':
        topwin()
button1=Button(root,text='lets get started!',command=msg,bg='brown',fg='white')
button1.place(x=260,y=360)
def topwin():
    top=Toplevel
    top.title("denomenasion caculater")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    label=Label(top,text="enter totel ammount",bg='light gray')
    entry=Entry(top)
    lbl=Label(top,text="Here is a number of notes for each denominasion",bg='light grey')
    l1=Label(top,text="2000",bg="light grey")
    l2=Label(top,text="500",bg="light grey")
    l3=Label(top,text="500",bg="light grey")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)