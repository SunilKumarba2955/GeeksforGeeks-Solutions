#User function Template for python3
import sys
sys.setrecursionlimit(10**5)
class Solution:
    def insertAtBottom(self,st,x):
        if not st:
            st.append(x)
        else:
            temp=st.pop()
            self.insertAtBottom(st,x)
            st.append(temp)
        return st

#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n,x = map(int,input().split())
        stack = list(map(int,input().split()))
        obj = Solution()
        ans = obj.insertAtBottom(stack,x)
        for e in ans:
            print(e,end=" ")
        print()
        
        
        
# } Driver Code Ends