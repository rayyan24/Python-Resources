from tkinter import *
from PIL import Image,ImageTk
root=Tk()
img=ImageTk.PhotoImage(Image.open("download.png"))
imageLabel=Label(image=img)
imageLabel.grid(row=0,column=0)
root.mainloop()