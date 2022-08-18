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

def main():
    a=revNum(1239)
    print(a)
if __name__=="__main__":
    main()