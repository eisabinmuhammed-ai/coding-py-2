from tkinter import *
from tkinter import messagebox
from  datetime import date
root=Tk()
root.title("getting started whith wingets")
root.geometry("400x500")
ibi=Label(text='hey there',fg="white",bg='red',height=1,width=296)
name_lbl=Label(text="did you do your homework\n",bg='blue')
name_entety=Entry()
name_lbl2=Label(text="did you go to play",bg='red')
name_entety2=Entry()
def display():
    name=name_entety.get()
    name2=name_entety2.get()
    global Message
    Message='Welcome to the applicasion\ntodays date is: '
    if name=='yes':
        greet='homework done\n'
    else:
         greet='homework not done\n'
         messagebox.showwarning("Do homework")
    if name2=='yes':
        greet2='went to play done\n'
    else:
         greet2='went to play not done\n'
         messagebox.showwarning("did not play")
    text_box.insert(END,greet2)
    text_box.insert(END,greet)
    text_box.insert(END,Message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text='disply',command=display,height=1,fg="white",bg="red")
ibi.pack()
name_lbl.pack()
name_lbl2.pack()
name_entety.pack()
name_entety2.pack()
btn.pack()
text_box.pack()
root.mainloop()