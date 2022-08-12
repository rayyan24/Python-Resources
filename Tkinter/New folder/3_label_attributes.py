from tkinter import *
root=Tk()
# change the title of GUI
root.title("GUI Title")
# label options
# Text-adds Text
# bd-background
# fg-foreground
# font-sets the font
# 1 font=("gigi",15,"bold")
# 2 font="gigi 15 bold"
# padx-x padding
# pady-y padding
# relief-border styling 1 SUNKEN RAISED GROOVE RIDGE
text_label=Label(text="Lorem Ipsum is simply dummy text of the printing and \ntypesetting industry. Lorem Ipsum has been the industry's standard dummy text \never since the 1500s, when an unknown printer took a galley of type and scrambled \nit to make a type specimen book. It has survived not only five centuries, but \nalso the leap into electronic typesetting, remaining essentially unchanged. It \nwas popularised in the 1960s with the release of Letraset sheets containing Lorem \nIpsum passages, and more recently with desktop publishing software like Aldus \nPageMaker including versions of Lorem Ipsum", 
bg="red",fg="white",padx=10,pady=10,font="gigi 15 bold",borderwidth=20,relief=RIDGE )
text_label.pack()

root.mainloop()