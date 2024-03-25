#User function Template for python3
class Solution:
    def __init__(self):
        self.ans_list = list()
    
    def solve(self,s,n,zero,one):
        if n == 0:
            self.ans_list.append(s)
            return
        
        self.solve(s+'1',n-1,zero,one+1)
        if one > zero:
            self.solve(s+'0',n-1,zero+1,one)
            
    
    def NBitBinary(self, n):
        # code here
        self.solve('1',n-1,0,1)
        return self.ans_list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends