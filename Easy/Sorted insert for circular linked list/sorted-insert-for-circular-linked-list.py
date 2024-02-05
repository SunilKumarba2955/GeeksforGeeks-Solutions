#User function Template for python3

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
        #code here
        node = Node(data)
        if not head:
            node.next = node
            return node
        elif head and head.next==head:
            node.next = head
            head.next = node
            if head.data >= data:
                return node
            return head
        temp = head
        prev = None
        while temp.next!=head:
            if temp.data > data:
                if not prev:
                    l = temp
                    while l.next!=temp:
                        l = l.next
                    l.next = node
                    node.next = temp
                    head = node
                else:
                    prev.next = node
                    node.next = temp
                return head
            prev = temp
            temp = temp.next
        if temp.data>=data:
            prev.next = node
            node.next = temp
            return head
        node.next = head
        temp.next = node
        if head.data >= data:
            return node
        return head


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        self.last=None
  
    # Function to insert a new node  
    def push(self, data):
        if not self.head:
            nn=Node(data)
            self.head=nn
            self.last=nn
            nn.next=nn
            return
        nn=Node(data)
        nn.next=self.head
        self.last.next=nn
        self.last=nn 
  

# Utility function to print the linked LinkedList

def printList(head):
    if not head:
        return
    temp = head 
    print (temp.data,end=' ') 
    temp = temp.next
    while(temp != head): 
        print (temp.data,end=' ') 
        temp = temp.next
  
    
if __name__ =='__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        data=int(input())

        cll=LinkedList()
        for e in arr:
            cll.push(e)
            
        reshead=Solution().sortedInsert(cll.head,data)
        printList(reshead)
        print()
        


# } Driver Code Ends