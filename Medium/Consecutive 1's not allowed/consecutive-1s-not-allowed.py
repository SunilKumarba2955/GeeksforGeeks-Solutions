#User function Template for python3
class Solution:

	def countStrings(self,n):
    	# code here
    	if n==1:
    	    return 2
    	if n==2:
    	    return 3
    	num1, num2 = 2,3
    	for i in range(3, n+1):
    	    num1, num2 = num2, (num1+num2)%(10**9+7)
    	return num2


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends