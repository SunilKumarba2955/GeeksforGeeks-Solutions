#User function Template for python3
import sys
sys.setrecursionlimit((10**5)//5)

class Solution:
    def func1(self,N,res,ref):
        if N<=0:
            res.append(N)
            return 
        res.append(N)
        self.func1(N-5,res,ref)
        
    def func2(self,N,res,ref):
        if N==ref:
            res.append(N)
            return
        res.append(N)
        self.func2(N+5,res,ref)
        
    def pattern(self, N):
        res=[]
        if (N<=0):
            res.append(N)
            return res
        else:
            ref=N
            self.func1(N,res,ref)
            if res[-1]<=0:
                self.func2(res[-1]+5,res,ref)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends