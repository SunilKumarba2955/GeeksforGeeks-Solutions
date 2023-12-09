#User function Template for python3

class Solution:
    def is_prime(self,n):
        if n==1:
            return False
        if n==2 or n==3:
            return True
        if n%2==0 or n%3==0:
            return False
        i=5
        while i*i<=n:
            if n%i==0 or n%(i+2)==0:
                return False
            i+=6
        return True
    
    def digit_sum(self,n):
        s=0
        while n:
            s+=n%10
            n//=10
        return s

    def prime_factor_sum(self,n):
        s=0
        k=n
        i=2
        flag=0
        while i*i<=k:
            while k%i==0:
                k//=i
                s+=self.digit_sum(i)
                flag=1
            i+=1
        if k>1 or not flag:
            s+=self.digit_sum(k)
        return s

    def smithNum(self, n):
        if n==1 or self.is_prime(n):
            return 0
        if self.digit_sum(n)==self.prime_factor_sum(n):
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends