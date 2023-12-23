#User function Template for python3
from collections import defaultdict

class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        hassh = defaultdict(int)
        s = set()
        count = 0
        for i in arr:
            hassh[i]+=1
            if hassh[i] > n//k and i not in s:
                count+=1
                s.add(i)
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends