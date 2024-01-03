#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here 
        tn = -1
        tnp1 = 0
        tnp2 = 0
        for i in range(N):
            cwtn = arr[i] & tn
            cwtnp1 = arr[i] & tnp1
            cwtnp2 = arr[i] & tnp2
            
            tn = tn & (~cwtn)
            tnp1 = tnp1|cwtn
            
            tnp1 = tnp1 & (~cwtnp1)
            tnp2 = tnp2 | cwtnp1
            
            tnp2 = tnp2 & (~cwtnp2)
            tn = tn | cwtnp2
        return tnp1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends