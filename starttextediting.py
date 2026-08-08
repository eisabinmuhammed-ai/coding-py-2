from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("Text editor")
window.geometry("544x456")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
def open_file():
    """editing open file"""
    filepath=askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    with open(filepath,"r")as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.title(f"Text editor-{filepath}")
def save_file():
    filepath=asksaveasfilename(defaultextension='txt',filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath,"w")as output_file:
        text=txt_edit.get(1.0,END)
        output_file.write(text)
    window.title(f"Text editor-{filepath}")
txt_edit=Text(window)
fr_butten=Frame(window,relief=RAISED,bd=2)
btn_opend=Button(fr_butten,text="opend",command=open_file)
btn_save=Button(fr_butten,text="save as...",command=open_file)
btn_opend.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_butten.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Start the GUI event loop
window.mainloop()