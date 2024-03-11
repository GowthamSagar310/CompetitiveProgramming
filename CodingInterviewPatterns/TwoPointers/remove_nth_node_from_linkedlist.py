def solve(head, n):
    left = head 
    right = head 
    for i in range(n):
        right = right.next 
    if not right: return head.next 
    while right:
        left = left.next 
        right = right.next
    left.next = left.next.next 
    return head 
