#User function Template for python3

class Solution:
	def nthPoint(self,n):
		# Code here
		n1 = 0
		n2 = 1
		for i in range(n):
		    n1, n2 = n2, (n1+n2)%(10**9+7)
		return n2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends