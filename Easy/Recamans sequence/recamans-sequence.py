#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        # code here
        seen = set([0])
        res = [0]
        prev = 0
        for i in range(1,n):
            term = prev-i
            if term>0 and term not in seen:
                prev = term
            else:
                prev = prev+i
            seen.add(prev)
            res.append(prev)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends