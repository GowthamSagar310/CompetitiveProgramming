# https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06

class Node:
    def __init__(self,val,next=None) -> None:
        self.val = val 
        self.next = next

head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)
head.next.next.next.next = head.next

# space O(n)
def solve(head):
    m = {}
    temp = head
    while temp:
        if temp in m:
            return True
        m[temp] = 1
        temp = temp.next
    return False 

# optimal approach
# slow and fast appoarches 
def solve_optimal(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow == fast: return True 
    return False