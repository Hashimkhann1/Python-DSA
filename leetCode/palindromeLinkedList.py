

class Node:
    
    def __init__(self , data):
        self.data = data
        self.next = None
    


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    # appedn Node
    def appendNode(self , data):
        
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        
        while current.next:
            current = current.next
        current.next = Node(data)
        
    def printAllNodes(self):
        
        current = self.head
        
        while current:
            print(current.data , end=' -> ')
            current = current.next
        print()

    # check if the Linked list is Palindrome
    def checkPalindrome(self):
        
        current = self.head
        slow = self.head
        fast = self.head
        
        # finding middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        
        # Reversing the half Linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left , right = self.head , prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True


l1 = LinkedList()
l1.appendNode(1)
l1.appendNode(2)
l1.appendNode(2)
l1.appendNode(1)
print(l1.checkPalindrome())
l1.printAllNodes()