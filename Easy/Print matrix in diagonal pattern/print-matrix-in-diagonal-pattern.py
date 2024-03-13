# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        temp = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(temp)==0 or len(temp)<=i+j:
                    temp.append([mat[i][j]])
                else:
                    temp[i+j].append(mat[i][j])
        res = []
        for i in range(len(temp)):
            if i%2==0:
                res.extend(temp[i][::-1])
            else:
                res.extend(temp[i])
        return res


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends