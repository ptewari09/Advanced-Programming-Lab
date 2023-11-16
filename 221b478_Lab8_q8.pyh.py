from tkinter import*

root=Tk()
root.title("Root Window")
root.geometry('500x500')
root.configure(bg="thistle")
Label(root,text="Let's Calculate").grid(row=0,column=0)
Label(root,text="Enter Number 1:").grid(row=1,column=0)
a=Entry(root)
a.grid(row=1,column=1)
Label(root,text="Enter Number 2:").grid(row=2,column=0)
b=Entry(root)
b.grid(row=2,column=1)
def add():
    c=int(a.get())+int(b.get())
    Label(root,text=c).grid(row=4,column=3)

def sub():
    d=int(a.get())-int(b.get())
    Label(root,text=d).grid(row=4,column=4)

def mult():
    m=int(a.get())*int(b.get())
    Label(root,text=m).grid(row=4,column=5)
def rem():
    r=int(a.get())%int(b.get())
    Label(root,text=r).grid(row=4,column=7)
def div():
    q=round(int(a.get())/int(b.get()),1)
    Label(root,text=q).grid(row=4,column=6)

Button(root,text="Addition",command=add).grid(row=3,column=3)
Button(root,text="Subtraction",command=sub).grid(row=3,column=4)
Button(root,text="Multiplication",command=mult).grid(row=3,column=5)
Button(root,text="Division",command=div).grid(row=3,column=6)
Button(root,text="Find Remainder",command=rem).grid(row=3,column=7)
root.mainloop()
