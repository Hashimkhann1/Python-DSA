


class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None



l1 = Node(10)
l2 = Node(20)
l3 = Node(30)
l4 = Node(40)
l5 = Node(50)


# linking the nodes
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5


current = l1

while current is not None:
    print(current.data)
    current = current.next
    
print('_____________________')    
print("Deletion in Linked list")
    

head = l1
head = head.next
current1 = head


while current1 is not None:
    print(current1.data)
    current1 = current1.next



print('_____________________')    
print("Deletion of list node from Linked list")

current2 = l1

while current2.next is not None:
    print(current2.data)
    current2 = current2.next
current2.next = None


def deleteParticularNode(node):
    current3 = l1
    
    while current3.data != node:
        print(current3.data)
        current3 = current3.next
    current3.next = current3.next


print('_____________________')    
print("Deletion of particular node")
deleteParticularNode(30)
    