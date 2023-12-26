from typing import List
from collections import defaultdict
class Solution:
    def sumZeroMatrix(self, mat : List[List[int]]) -> List[List[int]]:
        # code here
        maxi = 0 
        n = len(mat)
        m = len(mat[0])
        def maxlen(arr):
            hmap = defaultdict(int)
            hmap[0] = -1 
            sumi = 0
            maxlen = 0 
            top = -1
            bottom = -1
            for i in range(len(arr)):
                sumi += arr[i] 
                if sumi in hmap:
                    if i-hmap[sumi] > maxlen:
                        maxlen = i - hmap[sumi]
                        top = hmap[sumi] + 1
                        bottom = i
                    
                else:
                    hmap[sumi] = i 

            return [maxlen, top , bottom]
    
    
        def submatrix (tr, br, lc , rc):
            ans = []
            
            for i in range(tr, br+1):
                temp = []
                for j in range(lc, rc + 1):
                    temp.append(mat[i][j])
                ans.append(temp)
            return ans
                    
            
            
        maxarea = -1
        startrow = -1 
        startcol = -1
        endrow = -1 
        endcol = -1
        for i in range(m):
            rowSum = [0 for i in range(n)]
            for j in range(i,m):
                for k in range(n):
                    rowSum[k] += mat[k][j] 
                    
                values = maxlen(rowSum)
                
                length, top, bottom  = values[0], values[1], values[2]
                area = length * (j - i + 1)
                if area > maxarea:
                    # print(area, maxarea)
                    # print(top, bottom, i,j)
                    maxarea = area  
                    startrow = top 
                    endrow = bottom
                    startcol = i 
                    endcol = j 
                    
        if maxarea == -1 or  maxarea == 0:
            return []
        # print(startrow, endrow, startcol, endcol)
        # print (maxarea)
        return submatrix(startrow, endrow, startcol, endcol)


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



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        nm=IntArray().Input(2)
        
        
        a=IntMatrix().Input(nm[0], nm[1])
        
        obj = Solution()
        res = obj.sumZeroMatrix(a)
        if len(res) == 0:
            print(-1)
        else:
            IntMatrix().Print(res)
        

# } Driver Code Ends