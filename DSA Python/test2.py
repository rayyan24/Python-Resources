#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        temp=[]
        zero,one,two=0,0,0
        for i in arr:
            if i==0:
                zero+=1
                
            elif i==1:
                one+=1
                
            elif i==2:
                two+=1
            arr.remove(i)
        for i in range(one):
            arr.append(1)
        for j in range(two):
            arr.append(2)
        for k in range(zero):
            arr.append(0)
        arr.reverse()
        return arr

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends