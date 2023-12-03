#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    

# } Driver Code Ends
#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
   
    def countPairs(self, root1, root2, target_sum):
        nodes_set_1, nodes_set_2 = set(), set()

        def inorder_traversal(node, tree_number):
            if not node:
                return

            inorder_traversal(node.left, tree_number)

            if tree_number == 1:
                nodes_set_1.add(node.data)
            else:
                nodes_set_2.add(node.data)

            inorder_traversal(node.right, tree_number)

        # Perform inorder traversal for both BSTs
        inorder_traversal(root1, 1)
        inorder_traversal(root2, 0)

        result_count = 0

        # Count pairs with the given sum
        for value in nodes_set_1:
            result_count += 1 if target_sum - value in nodes_set_2 else 0

        return result_count

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s1=input()
        s2=input()
        root1=buildTree(s1)
        root2=buildTree(s2)
        x=int(input())
        ob = Solution()
        print(ob.countPairs(root1,root2,x))
# } Driver Code Ends