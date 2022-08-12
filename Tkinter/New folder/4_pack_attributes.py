from tkinter import *
root=Tk()
root.title("pack")
# pack attributes
# anchor=nw (must be n, ne, e, se, s, sw, w, nw, or center)
# side= top,bottom,left,right
# fill =X,Y stretch in x or y direction as we increase the window size
# padx
# pady

text_label=Label(text="Lorem Ipsum is simply dummy text of the printing and \ntypesetting industry. Lorem Ipsum has been the industry's standard dummy text \never since the 1500s, when an unknown printer took a galley of type and scrambled \nit to make a type specimen book. It has survived not only five centuries, but \nalso the leap into electronic typesetting, remaining essentially unchanged. It \nwas popularised in the 1960s with the release of Letraset sheets containing Lorem \nIpsum passages, and more recently with desktop publishing software like Aldus \nPageMaker including versions of Lorem Ipsum",bg="Green",fg="white")

text_label.pack(anchor="center",side="bottom",fill=Y,padx=100,pady=100)

root.mainloop()