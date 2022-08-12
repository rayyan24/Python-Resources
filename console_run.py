import tkinter 
from tkinter import filedialog
import os
i=1
while(i>0):
    main_win = tkinter.Tk()
    main_win.geometry("300x250")
    main_win.sourceFolder = ''
    main_win.sourceFile = ''

    def chooseFile():
        main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "G://College//C Language", title='Please select a directory')

    b_chooseFile = tkinter.Button(main_win, text = "Chose File", width = 20, height = 3, command = chooseFile)
    b_chooseFile.place(x = 50,y = 50)
    b_chooseFile.width = 100

    main_win.mainloop()
    a=(main_win.sourceFile)
