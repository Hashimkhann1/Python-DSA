


class Node:
    
    def __init__(self , data):
        self.data = data
        self.next = None


class Linkedlist:
    
    def __init__(self):
        self.head = None
        
    
    # appending new node
    def appendNode(self , data):
        
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    
    # Traversing in linked list
    def printList(self):
        current = self.head
        
        while current:
            print(current.data , end=' -> ')
            current = current.next
        print('None')
        
    
    # reversing the llinked list
    def reversingLinkedList(self):
        current = self.head
        prev = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        
    def deleteParticularNode(self , node_data):
            
        current = self.head
        previous = None
        
        # Check if head node is the one to be deleted
        if current is not None and current.data == node_data:
            
            self.head = current.next
            print(f"Deleted node with value {node_data} at head")
            return
        
        # Search for the node to delete, keeping track of previous node
        while current is not None and current.data != node_data:
            
            previous = current
            current = current.next
        
        if current is None:
            print(f'Node with value {node_data} not found.')
            return
        
        # Unlink the node to delete it
        previous.next = current.next
        print(f"Deleted node with value {node_data}")


    # add node at particular position
    def addNodeAtParticularPosition(self , new_node_data , position_node_data):
        
        new_node = Node(new_node_data)
        
        current = self.head
        
        while current is not None and current.data != position_node_data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        
        




l1 = Linkedlist()
l1.appendNode(10)
l1.appendNode(20)
l1.appendNode(30)
l1.appendNode(40)
l1.appendNode(50)


l1.printList()
l1.deleteParticularNode(40)
l1.printList()
l1.addNodeAtParticularPosition(100 , 20)
l1.printList()
l1.reversingLinkedList()
l1.printList()