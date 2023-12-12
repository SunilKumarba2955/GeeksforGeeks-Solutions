# User function Template for Python3

class Solution:
    def maxGold(self, rows, columns, gold_matrix):

        # Base cases when there is only one column or one row
        if columns == 1:
            return max(gold_matrix[i][0] for i in range(rows))
        elif rows == 1:
            return sum(gold_matrix[0])

        max_gold_collected = 0

        # Iterate over each column starting from the second column
        for col in range(1, columns):
            for row in range(rows):
                # Update the current cell with the maximum value from the adjacent cells in the previous column
                if row == 0:
                    gold_matrix[row][col] += max(gold_matrix[row][col-1], gold_matrix[row+1][col-1])
                elif row == rows - 1:
                    gold_matrix[row][col] += max(gold_matrix[row-1][col-1], gold_matrix[row][col-1])
                else:
                    gold_matrix[row][col] += max(gold_matrix[row-1][col-1], gold_matrix[row][col-1], gold_matrix[row+1][col-1])

                # Update the maximum amount of gold collected if the last column is reached
                if col == columns - 1:
                    max_gold_collected = max(max_gold_collected, gold_matrix[row][col])

        return max_gold_collected


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends