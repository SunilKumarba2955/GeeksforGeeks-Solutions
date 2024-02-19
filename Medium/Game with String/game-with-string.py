#User function Template for python3

from collections import Counter
import heapq
class Solution:
    def minValue(self, s, k):
        # code here
        counter_obj= Counter(s)
        
        sorted_arr = list(counter_obj.items())

        sorted_arr = sorted(sorted_arr, key=lambda x: x[1])
        list_data = [list(item[::-1]) for item in sorted_arr]
        heap = []
        for item in list_data:
            item[0] = -1*item[0] 
            heapq.heappush(heap, item)
        # print(list_data)
        while(k):
            ele = heapq.heappop(heap)
            ele[0] +=1 
            heapq.heappush(heap, ele)
            k-=1
        ans = 0
        for item in heap:
            ans += item[0] * item[0]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends