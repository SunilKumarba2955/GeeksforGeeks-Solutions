#User function Template for python3
class Solution:
    def kSubstrConcat(self, n, s, k):
        if n%k != 0:
            return 0
        i, j = 0, k
        while j<n:
            temp=s.replace(s[i:i+k], s[j:j+k], 1)
            x=0
            f=True
            while x<n:
                if (temp[x:(x+k)] != temp[(x+k):(x+(2*k))]) and temp[x:(x+k)] and temp[(x+k):(x+(2*k))]:
                    f=False
                    break
                x+=k
            if f:
                return 1
            i+=k
            j+=k
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends