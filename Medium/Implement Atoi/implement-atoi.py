#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,'8':8, '9':9}
        sign,res = 1,0
        for i in range(len(s)):
            if s[i]>='0' and s[i]<='9':
                res = res*10+dic[s[i]]
            elif s[i]=='-' and i==0:
                sign = -1
            else:
                return -1
        return res*sign

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends