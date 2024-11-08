
# Problem: Reverse a Linked List

# Description: Write a function to reverse a singly linked list. The function should take the head
# of a linked list as an input and return the head of the reversed linked list.


# Example
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL  
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL




class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)


l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

def reverse_linked_list(head: ListNode) -> ListNode:
    dummy = ListNode()
    head = dummy
    
    currnet = l1
    
    while currnet:
        head.next = currnet
        
        currnet = currnet.next
