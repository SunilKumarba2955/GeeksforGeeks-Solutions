#User function Template for python3

class Solution:
    def countWays(self,n,k):
        #code here.
        ans = 1
        prev = 1
        for i in range(1, n):
            temp = (k-1)*ans
            ans = (prev+temp)%(10**9+7)
            prev = temp
        return (ans*k)%(10**9+7)

#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends