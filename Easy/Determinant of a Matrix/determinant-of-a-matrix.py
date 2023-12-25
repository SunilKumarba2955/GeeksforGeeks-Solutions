
#User function Template for python3
MOD = 10**9+7

class Solution:
    
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,mat,n):
        # code here 
        if n == 1:
            return mat[0][0]
        
        res = 0
        for i in range(n):
            v = [ [0 for y in range(n-1)] for x in range(n-1) ]
            
            for j in range(1, n):
                curr = 0
                for k in range(n):
                    if k == i: 
                        continue
                    v[j-1][curr] = mat[j][k]
                    curr+=1

            if i%2 == 0:
                res += mat[0][i] * self.determinantOfMatrix(v, n-1)
            else:
                res -= mat[0][i] * self.determinantOfMatrix(v, n-1)
        return res
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends