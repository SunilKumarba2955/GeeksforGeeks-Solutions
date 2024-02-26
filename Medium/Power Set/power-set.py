#User function Template for python3

from itertools import combinations as cb
class Solution:
	def AllPossibleStrings(self, s):
		a=[]
		for i in range(1,len(s)+1):
		    for j in list(cb(s,i)):
		        a.append("".join(j))
        a.sort()
        return a


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends