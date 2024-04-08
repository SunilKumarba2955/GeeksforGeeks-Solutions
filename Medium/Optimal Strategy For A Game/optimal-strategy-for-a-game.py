#User function Template for python3


#Function to find the maximum possible amount of money we can win.
class Solution:
    def solve(self,s,e,arr):
        # if s+1==e:
        #     return max(arr[s-1],arr[e-1])
        # if s==e:
        #     return arr[s-1]
        if s>e:
            return 0
        return max( arr[s-1]+min(self.solve(s+2,e,arr), self.solve(s+1,e-1,arr)), arr[e-1]+ min(self.solve(s+1,e-1,arr),self.solve(s,e-2,arr)) )
    
    def optimalStrategyOfGame(self,n, arr):
        # return self.solve(1,n,arr)
        dp= [[None]*(n+1) for _ in range(n+1)]
        start=(n+1)%2
        for gap in range(start,n,2):
            for i in range(1,n+1-gap):
                j= i+gap
                if gap==0:
                    dp[i][j]=arr[i-1]
                elif gap==1:
                    dp[i][j]=max(arr[i-1],arr[j-1])
                else:
                    dp[i][j]=max(   arr[i-1]+ min(dp[i+2][j],dp[i+1][j-1]),arr[j-1]+min(dp[i+1][j-1],dp[i][j-2])    )
        return dp[1][n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))

# } Driver Code Ends