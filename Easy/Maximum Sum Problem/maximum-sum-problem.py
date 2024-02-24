#User function Template for python3

class Solution:
        
    def maxSum(self, n): 
        
        a = n // 2
        b = n // 3
        c = n // 4
        if a + b + c > n:
            return self.maxSum(a) + self.maxSum(b) + self.maxSum(c)
        return n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends