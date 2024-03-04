class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

# while head:
#     print(head.val)
#     head = head.next

def solve(head):
    if not head: return None
    newhead = ListNode(head.val)
    temp = newhead 
    prev = head.val
    head = head.next
    while head:        
        if prev != head.val:
            newhead.next = ListNode(head.val)
            newhead = newhead.next
            prev = head.val
        head = head.next
    return temp 

newhead = solve(head)
while newhead:
    print(newhead.val)
    newhead = newhead.next
