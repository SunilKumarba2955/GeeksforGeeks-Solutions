#User function Template for python3
MOD = 10**9+7

class Solution:
    def sumSubstrings(self,s):
        last=0
        n=len(s)
        mod=10**9+7
        ab=0
        for i in range(n):
            val=int(s[i])
            ab=((ab*10)+val*(i+1))%mod
            last=(last+ab)%mod
        return last 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends