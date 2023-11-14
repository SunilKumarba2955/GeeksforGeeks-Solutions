#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1)!=len(str2):
            return 0
        n=len(str1)
        map1,map2=dict(),dict()
        for i in range(n):
            if str1[i] in map1:
                if map1[str1[i]]!=str2[i]:
                    return 0
            else:
                map1[str1[i]]=str2[i]
            if str2[i] in map2:
                if map2[str2[i]]!=str1[i]:
                    return 0
            else:
                map2[str2[i]]=str1[i]
        return 1
                




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends