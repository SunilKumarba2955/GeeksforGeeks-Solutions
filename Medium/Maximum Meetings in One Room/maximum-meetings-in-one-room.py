from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        res = []
        for i in range(N):
            res.append([i+1, S[i], F[i]])
        res = sorted(res, key = lambda x: x[2])
        et = res[0][2]
        ans = [res[0][0]]
        for i in range(1, len(res)):
            st = res[i][1]
            if st>et:
                ans.append(res[i][0])
                et = res[i][2]
        return sorted(ans)
                



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends