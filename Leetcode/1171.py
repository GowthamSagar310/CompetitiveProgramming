# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/?envType=daily-question&envId=2024-03-12

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val 
        self.next = next 

head = Node(5, Node(-3, Node(-4, Node(1, Node(6, Node(-2, Node(-5)))))))

def solve(head):
    dummy = Node(0, head)
    prefix = 0
    map = {0: dummy}
    while head:
        prefix += head.val 
        map[prefix] = head 
        head = head.next 
    prefix = 0
    head = dummy 
    while head:
        prefix += head.val 
        head.next = map[prefix].next 
        head = head.next 
    return dummy.next 
