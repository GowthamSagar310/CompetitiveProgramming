# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val 
        self.next = next 

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

def solve(head):
        if not head or not head.next: return None 
        fast = head 
        slow = head 
        prev = None 
        while fast and fast.next:
            fast = fast.next.next 
            prev = slow 
            slow = slow.next 
        prev.next = prev.next.next 
        return head 

head = solve(head)
while head:
    print(head.val)
    head = head.next 
