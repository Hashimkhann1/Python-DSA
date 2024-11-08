


class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    
    def appendNode(self , data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        
        while current.next:
            current = current.next
        current.next = new_node

    # appending node at the begganing
    def appendNodeAtTheBeggining(self , data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
    
    # deleting the node
    def deleteNode(self , data):
        
        current = self.head
        previous = None
        
        # checkin if first node is equal to data s delete it
        if current is not None and current.data == data:
            self.head = current.next
            return
        
        # travering through all nodes
        while current is not None and current.data != data:
            
            previous = current
            current = current.next
        
        # if node is found
        if current is None:
            print(f'Node with value {data} not found.')
            return
        
        # deleting the node
        previous.next = current.next
        print(f"Deleted node with value {data}")
    
    # searching for node
    def searchForNode(self , data):
        
        current = self.head
        
        if current is not None and current.data == data:
            self.head = current.next
            return
        
        while current is not None:
            if current.data == data:
                break
            current = current.next
        
        if current is None:
            print(f'Node with value {data} not found.')
            return
            
        print(f"Node is found {current.data}")
    
    # count nodes in the linked list
    def countNodes(self):
        nodes = 0
        current = self.head
        
        while current is not None:
            nodes += 1
            current = current.next
        
        return nodes
    
    # reversing the linked list
    def reversingLinkedList(self):
        
        current = self.head
        prev = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
    
    # prinal all nodes
    def printAllNodes(self):
        
        current = self.head
        
        while current:
            print(current.data , end=' -> ')
            current = current.next
        print()


l1 = LinkedList()
l1.appendNode(10)
l1.appendNode(20)
l1.appendNode(30)
l1.appendNode(40)

l1.printAllNodes()
l1.appendNodeAtTheBeggining(50)
l1.printAllNodes()

# >>>>>>>> deleting the node >>>>>>>>>
# l1.deleteNode(20)
# l1.printAllNodes()


# >>>>>>>> searching for node >>>>>>>>>>>>
# l1.searchForNode(30)


# >>>>>>>> counting node in the linked list >>>>>>>>
# print(l1.countNodes())


l1.reversingLinkedList()
l1.printAllNodes()

