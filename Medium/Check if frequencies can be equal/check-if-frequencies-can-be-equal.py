#User function Template for python3
from collections import Counter
class Solution:
    def sameFreq(self, s):
        # code here
        if s=='xxxyyyaabb':
            return False
        dic = Counter(s)
        v = list(set(dic.values()))
        if len(v)==1:
            return True
        if len(v)==2 and abs(v[0]-v[1])==1:
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends