def solve_optimal(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow == fast: return True 
    return False