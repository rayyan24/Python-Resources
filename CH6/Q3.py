text=input("Enter Text ")
if ("fool" in text):
    spam=True
elif ("useless" in text):
    spam=True
elif ("nonsense" in text):
    spam=True
else:
    spam=False
    
if (spam):
    print("spam is present")
else :
    print("No Spam")