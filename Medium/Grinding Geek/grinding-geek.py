
from typing import List


class Solution:
    def __init__(self):
        pass
    
    def helper(self, i, cost, total, n, dp):
        if total <= 0:
            return 0
        if i == n:
            return 0

        # if entry already exists in dp, then return the existing value
        if dp[i][total] != -1:
            return dp[i][total]

        a, b = 0, 0

        # Case when we can buy the course and we actually buy the course
        if cost[i] <= total:
            a = 1 + self.helper(i + 1, cost, int(total - cost[i] * 0.1), n, dp)

        # Case when we don't buy the course
        b = self.helper(i + 1, cost, total, n, dp)

        dp[i][total] = max(a, b)

        return dp[i][total]

    def max_courses(self, n, total, cost):
        # DP matrix
        dp = [[-1] * (total + 1) for _ in range(n + 1)]
        return self.helper(0, cost, total, n, dp)
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        total = int(input())
        
        
        cost=IntArray().Input(n)
        
        obj = Solution()
        res = obj.max_courses(n, total, cost)
        
        print(res)
        

# } Driver Code Ends