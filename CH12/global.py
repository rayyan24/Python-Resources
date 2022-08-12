a=10 # global variable
def gb():
    global a # give the function permission to read and write global variable(out of the functions)
    # a=11
    print(a) # local variable
gb()
a=18
print(a)