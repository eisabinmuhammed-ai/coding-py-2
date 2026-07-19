from tkinter import *
from  datetime import date
root=Tk()
root.title("getting started whith wingets")
root.geometry("400x300")
ibi=Label(text='hey there',fg="white",bg='red',height=1,width=296)
name_lbl=Label(text="full name",bg='blue')
name_entety=Entry()
def display():
    name=name_entety.get()
    global Message
    Message='Welcome to the applicasion\ntodays date is: '
    greet='hello'+name+'\n'
    text_box.insert(END,greet)
    text_box.insert(END,Message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text='disply',command=display,height=1,fg="white",bg="red")
ibi.pack()
name_lbl.pack()
name_entety.pack()
btn.pack()
text_box.pack()
root.mainloop()