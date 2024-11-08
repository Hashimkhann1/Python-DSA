


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4


current = node1

while current is not None:
    print(current.data , end=' -> ')
    current = current.next
    
print()
print()
print("-----------------")
print("Insertion And at the beginning of Linked list")


head = node1
new_node = Node(1)
new_node.next = head
head = new_node
currentT = head

while currentT is not None:
    print(currentT.data , end=' -> ')
    currentT = currentT.next

print()
print()
print('------------------------')
print("Deletion in Linked list")


head1 = Node(100)
l2 = Node(200)
l3 = Node(300)
l4 = Node(400)
l5 = Node(500)

head1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

# deletioin of first node

# if head1 is not None:
    # head1 = head1.next

current1 = head1

# deletioin of first node

# while current1 is not None:
#     print(current1.data, end=' ')
#     current1 = current1.next


while current1.next is not None:
    print(current1.data , end=' ')
    current1 = current1.next
current1.next = None