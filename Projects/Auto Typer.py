import pyautogui as auto
import time
from tkinter import filedialog
def chooseFile():
    return filedialog.askopenfilename()
fileRead=chooseFile()
print("Enter 1 for Slow Speed")
print("Enter 2 for Medium Speed")
print("Enter 3 for Fast Speed")
speed=int(input())
for i in range(1,6):
    print(i)
    time.sleep(1)
if(speed==1):
    with open(fileRead,"r") as file1:    
        for line in file1:
            for character in line:
                auto.typewrite(character)
            auto.press("enter")
elif(speed==2):
    with open(fileRead,"r") as file1:    
        for line in file1:
                auto.typewrite(line)
                auto.press("enter")
                time.sleep(0.3) 
elif(speed==3):
    with open(fileRead,"r") as file1:    
        a=file1.read()
        auto.typewrite(a)
        auto.press("enter")
