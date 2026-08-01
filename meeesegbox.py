from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("150x250")
def msg():
    messagebox.showwarning("Alart","Stop! virses")
button=Button(root,text="scan for vires",command=msg)
button.pack()
root.mainloop()
