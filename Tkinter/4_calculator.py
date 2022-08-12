from tkinter import *
root=Tk()
root.title("Calculator")
textbox=Entry(root,width=39)
textbox.grid(row=0,column=0,columnspan=3)
def num_btn(num):
    now=textbox.get()
    textbox.delete(0,END)
    textbox.insert(0, str(now)+str(num))
def clear():
    textbox.delete(0,END) 
global fnum
global operation
operation=""
def plus():
    global operation
    global fnum
    fnum=int(textbox.get())
    operation="+"
    textbox.delete(0,END)
def minus():
    global fnum
    global operation
    fnum=int(textbox.get())
    operation="-"
    textbox.delete(0,END)
def multiply():
    global fnum
    global operation
    fnum=int(textbox.get())
    operation="*"
    textbox.delete(0,END)
def divide():
    global fnum
    global operation
    fnum=int(textbox.get())
    operation="/"
    textbox.delete(0,END)
    
def equal():
    global operation
    second_num=textbox.get()
    textbox.delete(0,END)
    if(operation=="+"):
        textbox.insert(0,int(fnum)+int(second_num))
    elif(operation=="-"):
        textbox.insert(0,int(fnum)-int(second_num))
    elif(operation=="*"):
        textbox.insert(0,int(fnum)*int(second_num))
    elif(operation=="/"):
        textbox.insert(0,int(fnum)/int(second_num))
# Define Buttons
btn_1=Button(root,text="1",padx=30,pady=10,borderwidth=3,command=lambda:num_btn(1))
btn_2=Button(root,text="2",padx=30,pady=10,borderwidth=3,command=lambda:num_btn(2))
btn_3=Button(root,text="3",padx=30,pady=10,borderwidth=3,command=lambda:num_btn(3))
btn_4=Button(root,text="4",padx=30,pady=10,borderwidth=3,command=lambda:num_btn(4))
btn_5=Button(root,text="5",padx=30,pady=10,borderwidth=3,command=lambda:num_btn(5))
btn_6=Button(root,text="6",padx=30,pady=10,borderwidth=3,command=lambda:num_btn(6))
btn_7=Button(root,text="7",padx=30,pady=10,borderwidth=3,command=lambda:num_btn(7))
btn_8=Button(root,text="8",padx=30,pady=10,borderwidth=3,command=lambda:num_btn(8))
btn_9=Button(root,text="9",padx=30,pady=10,borderwidth=3,command=lambda:num_btn(9))
btn_0=Button(root,text="0",padx=110,pady=10,borderwidth=3,command=lambda:num_btn(0))
btn_plus=Button(root,text="+",padx=30,pady=10,borderwidth=3,command=plus)
btn_minus=Button(root,text="-",padx=30,pady=10,borderwidth=3,command=minus)
btn_multiply=Button(root,text="*",padx=30,pady=10,borderwidth=3,command=multiply)
btn_divide=Button(root,text="/",padx=30,pady=10,borderwidth=3,command=divide)
btn_clear=Button(root,text="CLEAR",padx=15,pady=10,borderwidth=3,command=clear)
btn_equal=Button(root,text="=",padx=30,pady=10,borderwidth=3,command=equal)
# Positioning Buttons
btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)
btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)
btn_0.grid(row=4,column=0,columnspan=3)
btn_plus.grid(row=5,column=0)
btn_minus.grid(row=5,column=1)
btn_multiply.grid(row=6,column=0)
btn_divide.grid(row=6,column=1)
btn_clear.grid(row=5,column=2)
btn_equal.grid(row=6,column=2)
root.mainloop()