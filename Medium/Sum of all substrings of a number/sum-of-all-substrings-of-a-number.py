#User function Template for python3
MOD = 10**9+7

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        # code here
        res = 0
        prev = 0
        
        for i in range(len(s)):
            curr = int(s[i])
            prev = ((prev*10)+curr*(i+1))%MOD
            res = (res + prev)%MOD
        return res


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