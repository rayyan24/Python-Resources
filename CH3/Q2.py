a=input("Enter Name\n")
b=input("Enter Date\n")
letter='''Dear <|Name|>
You are selected 
<|Date|>'''
letter=letter.replace("<|Name|>",a)
letter=letter.replace("<|Date|>",b)
print(letter)
