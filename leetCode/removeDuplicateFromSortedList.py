


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# l1 = ListNode(1)
# l2 = ListNode(1)
# l3 = ListNode(2)
# l4 = ListNode(3)
# l5 = ListNode(3)

l1 = ListNode(10)
l2 = ListNode(20)
l3 = ListNode(50)
l4 = ListNode(30)
l5 = ListNode(40)
l6 = ListNode(50)
l7 = ListNode(60)


l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7


# def removeDuplicateItems(lis1):
    
current = l1
prev = None
re = 50

if current is not None and current.val == re:
    current = current.next
print(current.val)

while current is not None and current.next is not None:
    if current.next.val == re:
        current.next = current.next.next
    else:
        current = current.next
    print(current.val)
    
    