#User function Template for python3
import sys
sys.setrecursionlimit(10**6)
class Solution:
    def sequence(self, n, start=2, count=2):
        # code here
        if n==1:
            return 1
        res = 1
        for _ in range(count):
            res = (res*start)%(10**9+7)
            start+=1
        return (res+self.sequence(n-1, start, count+1))%(10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends