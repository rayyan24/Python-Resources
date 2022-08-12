d1={
'english':13,
'hindi':14,
'urdu':9,
"d2":{'A':1,'B':2,'C':{1,2,3}},
'good':False
}
a=d1.keys() # type of this variable is dict keys 
a=list(a)      
print(a)
print(list(d1.keys()))
b=d1.values() # type of this variable is dict values
b=list(b)
print(b)
print(list(d1.values()))
c=d1.items() # type of this variable is dict items.gives the whole dictionary 
c=list(c)
print(c)
A={"alpha":1,'beta':2}
d1.update({"alpha":1})
d1.update(A)
print(d1)
print(d1["english"])
print(d1.get("english"))
# in case english is not present in the dictionary .get will return none while [] will return an error