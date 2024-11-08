


class Node:
    def __init__(self , data):
        self.data = data
        self.next = None



class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def appendNode(self , data):
        
        if self.head is None:
            self.head = Node(data)
            return
        
        current = self.head
        
        while current.next:
            current = current.next
        current.next = Node(data)
    
    def reveerseLinkedLList(self):
        
        current = self.head
        prev = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        
    def checkLinkedListIspalindrome(self):
        
        holdNode = []
        current = self.head
        
        while current:
            holdNode.append(current.data)
            current = current.next
        
        print(holdNode == holdNode[::-1])
    
    def findMiddleNode(self):
        
        slow , fast = self.head ,self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def printAllNodes(self):
        
        current = self.head
        
        while current:
            print(current.data , end=' -> ')
            current = current.next
        print()



l1 = LinkedList()
l1.appendNode(1)
l1.appendNode(2)
l1.appendNode(2)
l1.appendNode(1)
# l1.appendNode(50)

l1.printAllNodes()
# l1.checkLinkedListIspalindrome()
# l1.printAllNodes()

print(l1.findMiddleNode())