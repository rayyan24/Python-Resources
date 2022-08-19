def nums(n):
    if n==0:
        return
    nums(n-1)
    print(n)
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
def SUM(n:int):
    if n<=1:
        return n
    return n+SUM(n-1)
def digitSum(n):
    if n<=9:
        return n
    return n%10 +digitSum(n//10)
def revNum(n):
    if n<=9:
        return n 
    digits=len(str(n))
    return (n%10)*10**(digits-1)+revNum(n//10)
Sum=0
def revNUM(n):
    global Sum
    if n==0:
        return 0  
    lastDigit=n%10
    Sum=Sum*10+lastDigit
    revNUM(n//10)
def countZeros(n,count=0):
    if n==0:
        return count
    elif n%10==0:
        return countZeros(n//10,count+1)
    else:
        return countZeros(n//10,count)
def checkSorted(arr:list[int]):
    def helper(arr,size,curElem=0):
        if curElem==size: 
            return True
        elif arr[curElem]>arr[curElem+1]:
            return False
        else:
            return helper(arr,size,curElem+1)
    size=len(arr)-1
    return helper(arr,size)  


def main():
    a=checkSorted([21,2,3,4,5,12,65,1])
    print(a)
if __name__=="__main__":
    main()