

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        res = []
        for i in range(len(price)):
            res.append([price[i], i+1])
        res = sorted(res, key = lambda x:x[0])
        # print(res)
        ans=0
        for i in res:
            if k<i[0]:
                break
            if (k//i[0])>i[1]:
                ans+=i[1]
                k-= i[1] * i[0]
            else:
                ans+= k//i[0]
                k-= k/i[0]*i[0]
        return ans


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
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends