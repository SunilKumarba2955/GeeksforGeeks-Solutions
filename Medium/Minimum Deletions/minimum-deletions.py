#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self, input_string):
        string_length = len(input_string)
        dp = [[0] * string_length for _ in range(string_length)]
        for i in range(string_length):
            dp[i][i] = 1
        for substring_length in range(2, string_length + 1):
            for start_index in range(string_length - substring_length + 1):
                end_index = start_index + substring_length - 1
                if input_string[start_index] == input_string[end_index] and substring_length == 2:
                    dp[start_index][end_index] = 2
                elif input_string[start_index] == input_string[end_index]:
                    dp[start_index][end_index] = dp[start_index + 1][end_index - 1] + 2
                else:
                    dp[start_index][end_index] = max(dp[start_index][end_index - 1], dp[start_index + 1][end_index])
       
        return string_length - dp[0][string_length - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends