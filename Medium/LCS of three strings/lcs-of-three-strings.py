#User function Template for python3

class Solution:
    def lcs(self, s1, s2, s3, l, m, n, memo):
        if l == 0 or m == 0 or n == 0:
            return 0
        if (l, m, n) in memo:
            return memo[(l, m, n)]
        if s1[l - 1] == s2[m - 1] and s2[m - 1] == s3[n - 1]:
            memo[(l, m, n)] = 1 + self.lcs(s1, s2, s3, l-1, m-1, n-1, memo)
        else:
            memo[(l, m, n)] = max(
                self.lcs(s1, s2, s3, l-1, m, n, memo),
                self.lcs(s1, s2, s3, l, m-1, n, memo),
                self.lcs(s1, s2, s3, l , m, n-1, memo)
            )
        return memo[(l, m, n)]
        
    def LCSof3(self,s1, s2, s3, l, m, n):
        # code here
        return self.lcs(s1, s2, s3, l, m, n, {})

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends