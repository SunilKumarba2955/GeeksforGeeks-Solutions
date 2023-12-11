#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        res = 0
        for i in range(K):
            res+=Arr[i]
        maxSum = res
        for i in range(K, N):
            res+=Arr[i]-Arr[i-K]
            maxSum = max(res, maxSum)
        return maxSum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends