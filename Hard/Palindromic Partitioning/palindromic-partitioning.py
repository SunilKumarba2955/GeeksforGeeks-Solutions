#User function Template for python3

class Solution:
    def palindromicPartition(self, input_string):
        string_length = len(input_string)
        min_cuts = [0] * string_length
        def is_palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        for i in range(string_length):
            min_partition_cuts = i
            for j in range(i, -1, -1):
                if is_palindrome(input_string, j, i):
                    min_partition_cuts = 0 if j == 0 else min(min_partition_cuts, 1 + min_cuts[j - 1])
            min_cuts[i] = min_partition_cuts
        return min_cuts[string_length - 1]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends