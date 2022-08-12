def countMin(Str):
    count={}
    for i in Str:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    finalCount=0
    for val in list(count.values()):
        if val%2==0:
            continue
        else:
            finalCount+=val
    if finalCount%2==0:
        return finalCount-1
    else:
        return finalCount

    
def main():
    print(sorted("sfdsffdsf"))
    a=countMin("abcd")
    print(a)
    a=countMin("anasdad")
    print(a)
main()