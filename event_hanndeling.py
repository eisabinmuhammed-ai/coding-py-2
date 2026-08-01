from tkinter import *
window=Tk()
window.title('event hanndeling')
window.geometry('100x100')
def handle_keypress(event):
    """print assosieted hanndeling"""
    print(event.char)
window.bind("<Key>",handle_keypress)
def handel_click(event):
    print("\nThe butten was clicked")
button=Button(text='click me')
button.pack()
button.bind('<Button-1>',handel_click)
window.mainloop()