from tkinter import *
from PIL import ImageTk, Image

root = Tk()
img1 = ImageTk.PhotoImage(Image.open("a.png"))
img2 = ImageTk.PhotoImage(Image.open("b.png"))
img3 = ImageTk.PhotoImage(Image.open("c.png"))
img4 = ImageTk.PhotoImage(Image.open("d.png"))
img5 = ImageTk.PhotoImage(Image.open("e.png"))
img_list = [img1, img2, img3, img4, img5]
image_num = 0
def forward():
    global imageLabel, image_num, img_list
    image_num = image_num + 1
    print(f"{image_num}")
    if image_num ==  (len(img_list)):
        forward_btn = Button(root, text=">>", command=forward, state=DISABLED)
        forward_btn.grid(row=1, column=2)
    else:
        imageLabel.grid_forget()
        imageLabel = Label(root, image=img_list[image_num])
        forward_btn = Button(root, text=">>", command=forward)
        forward_btn.grid(row=1, column=2)
        imageLabel.grid(row=0, column=0, columnspan=3)


def back():
    global imageLabel, image_num, img_list
    if image_num<=0:
        back_btn = Button(root, text="<<", command=back,state=DISABLED)
        back_btn.grid(row=1, column=0)
    else:
        imageLabel.grid_forget()
        image_num -= 1
        imageLabel = Label(root, image=img_list[image_num])
        forward_btn = Button(root, text=">>", command=forward)
        forward_btn.grid(row=1, column=2)
        imageLabel.grid(row=0, column=0, columnspan=3)


imageLabel = Label(root, image=img_list[image_num])
back_btn = Button(root, text="<<", command=back)
forward_btn = Button(root, text=">>", command=forward)

imageLabel.grid(row=0, column=0, columnspan=3)
back_btn.grid(row=1, column=0)
forward_btn.grid(row=1, column=2)
root.mainloop()