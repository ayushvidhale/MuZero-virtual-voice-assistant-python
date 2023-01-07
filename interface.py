from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
root.title("MuZero")
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

  
# Demo function 1
def fun1():
    print("Function 1")
  
  
# Demo function 2
def fun2():
    print("Function 2")
  

ttk.Button(frm, text="Start", command=lambda: [fun1(), fun2()]).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)


root.mainloop()