from tkinter import *
root=Tk()
root.quit()
def work():
    l1=Label(root,text="By Press Of Button")
    l1.grid()
btn1=Button(root,command=work,text="click me")
btn2=Button(root,text="CLICK HERE",bg="green",fg="Red")

btn1.grid(row=0,column=3)
btn2.grid(row=0,column=4)
root.mainloop()