from tkinter import *
# give the starting size of window takes arguement as"widthxheight" in pixels
root=Tk()
root.geometry("500x500")
# minimum size a window can be sized width,height
root.minsize(100,100)
# maximum size a window can be sized width,height
root.maxsize(800,700)
# add some text in the GUI
label1=Label(text="Hello How Are You")
label1.pack()

# command to start the GUI of the code 
root.mainloop()
