from tkinter import *
root=Tk()
root.title("TITLE")
# defining icon 
root.iconbitmap("icon.ico")
# creatin an exit button
Exit=Button(root,text="Exit",command=root.quit)
Exit.pack()
root.mainloop()