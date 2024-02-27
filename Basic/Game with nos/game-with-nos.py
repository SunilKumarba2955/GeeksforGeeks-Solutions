#User function Template for python3

def game_with_number (arr,  n) : 
    #Complete the function
    return [ arr[i]^arr[i+1] for i in range(n-1)]+[arr[n-1]]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends