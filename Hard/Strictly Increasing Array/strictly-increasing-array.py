#User function Template for python3

class Solution:
    def lis(self, nums, n):
        dp = [0]*n
        dp[0] = 1
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < 1 + dp[j] and (i - j) <= nums[i] - nums[j]:
                    dp[i] = 1 + dp[j]
        ans = 1
        for i in range(n):
            ans = max(ans, dp[i])
        return ans
	def min_operations(self,nums):
        n = len(nums)
        return n - self.lis(nums, n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.min_operations(nums)
		print(ans)
# } Driver Code Ends