# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=daily-question&envId=2024-03-03

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val 
        self.next = next 

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# brute force. 
# get the length.
# then go up to (length - k) node, let it be temp
# delnode = temp.next 
# delnode = None
# temp.next = temp.next.next 
# travelling twice, O(2 * len(ll))

# optimal 

k = 2 

def solve(head, k):
    fast = head 
    slow = head 

    for _ in range(k):
        fast = fast.next 

    if not fast: 
        return head.next 

    while fast.next:
        fast = fast.next 
        slow = slow.next

    slow.next = slow.next.next

    while head:
        print(head.val)
        head = head.next 
    
    return head

head = solve(head, k)
while head:
    print(head.val)
    head = head.next 
