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
def linearSearch(arr,target,index=0)->int:
    if index>len(arr):
        return -1
    elif arr[index]==target:
        return index
    else:
        return linearSearch(arr,target,index+1)
def linearSearch_(arr,target)->list[int]:
    # occurances=[]
    # def helper(arr,target,index=0):
    #     if index>len(arr):
    #         return 
    #     elif arr[index]==target:
    #         occurances.append(index)
    #     helper(arr,target,index+1)
        
    # helper(arr,target)
    # return occurances
    occurances=[]
    s=len(arr)
    def helper(arr,t,index=0,size=s):
        if index==size:
            return
        if arr[index]==target:
            occurances.append(index)
        helper(arr,t,index+1,s)
    helper(arr,target,0,s)
    return occurances if len(occurances)!=0 else -1
def rotatedBinarySearch(arr,target,start,end):
    if start>end:
        return -1
    mid=(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>= arr[start]:
        if target<=arr[mid] and target>=arr[start]:
            return rotatedBinarySearch(arr,target,start,mid-1)
        else:
            return rotatedBinarySearch(arr,target,mid+1,end)
    else:
        if target>=arr[mid] and target<=arr[end]:
            return rotatedBinarySearch(arr,target,mid+1,end)
        else:
            return rotatedBinarySearch(arr,target,start,mid-1)






    


def main():
    a=rotatedBinarySearch([4,5,6,7,0,1,2],2,0,6)
    print(a)
if __name__=="__main__":
    main()