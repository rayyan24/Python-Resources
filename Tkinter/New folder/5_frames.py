from tkinter import * 
root=Tk()
root.title("Frames")
root.geometry("400x400")
# adding frame in GUI usage -->frame1=(name_of_tk_instance,any other arguements like bg fg padx pady)
frame1=Frame(root,bg="red",borderwidth=10,relief=SUNKEN)
frame1.pack(side=LEFT,fill="y")
# adding label to the frame --> label1=(name_of_in_which_it_is_to_be_added ,any other arguements like bg fg padx pady)
text1=Label(frame1,text="HELLO TK")
text1.pack(pady=150,fill="y")


frame2=Frame(root,borderwidth=10,bg="red",relief=SUNKEN)
frame2.pack()
text2=Label(frame2,text="Hello From TK")
text2.pack(padx=100,fill="x")
root.mainloop()