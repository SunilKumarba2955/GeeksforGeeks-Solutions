#User function Template for python3

class Solution:
    def repeatedRows(self, arr, m ,n):
        dp={}
        ans=[]
        for i in range(len(arr)):
            t=tuple(arr[i])
            if dp.get(t,0)==0: # not seen before, add to dp
                dp[t]=1
            else: # seen this row before, add to ans
                ans.append(i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        arr = []
        for i in range(n):
            nums = list(map(int, input().strip().split()))
            arr.append(nums)
        ob = Solution()
        ans = ob.repeatedRows(arr, n, m)
        
        for x in ans:
            print(x, end=" ")
            
        print()
        tc -= 1

# } Driver Code Ends