from tkinter import *
root=Tk()
label1=Label(root,text="Enter First Number")
label1.grid(row=0,column=0)
label1=Label(root,text="Enter Second Number")
label1.grid(row=1,column=0)
inp1=Entry(root)
inp1.grid(row=0,column=1)
inp2=Entry(root)
inp2.grid(row=1,column=1)
def calculate():
    try:
        tempLabel=Label(root,text=int(inp1.get())+int(inp2.get()))
        tempLabel.grid(row=3,column=1)
    except Exception as e:
        tempLabel=Label(root,text="Enter Valid Numbers")
        tempLabel.grid(row=4,column=1)
btn1=Button(root,command=calculate,text="Calculate")
btn1.grid(row=3,column=2)
root.mainloop()