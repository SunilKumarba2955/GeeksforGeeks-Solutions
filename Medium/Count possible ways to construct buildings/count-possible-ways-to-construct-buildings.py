#User function Template for python3

class Solution:
	def TotalWays(self, N):
		# Code here
		MOD = 10**9+7
		a,b=1,1
		for i in range(1, N+1):
		    cur = (a+b)%MOD
		    a = b
		    b = cur
		return (b*b)%MOD


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends