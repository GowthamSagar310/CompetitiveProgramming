# linkedlist 

# basic node class
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data 
        self.next = next

# 4 -> 2 -> 3 -> 1 -> 0 -> 5
# 4 --> head 
# 4 --> tail 

# convertion of arr in linkedlist

def convert_to_linkedlist(arr):
    if not arr: return None # len = 0 case
    head = Node(arr[0])
    previous_node = head
    for i in range(1, len(arr)):
        current_node = Node(arr[i])
        previous_node.next = current_node
        previous_node = current_node
    return head

def print_linkedlist(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# test
arr = [4, 2, 3, 1, 0, 5]
head = convert_to_linkedlist(arr)
print_linkedlist(head)

# insert at head 
def insert_node_at_beginning(head, value):
    # node = Node(value)
    # node.next = head 
    # return node # node itself is head 
    return Node(value, head)

# insert at end
def insert_node_at_last(head, value):
    if head is None: return Node(value)
    current = head 
    while current.next:
        current = current.next
    current.next = Node(value)
    return head 

# insert at kth position
def insert_node_at_kth_pos(head, value, k):
    if head is None:
        return Node(value) if k == 1 else None
    if k == 1:
        return Node(value, head)
    count = 0
    current = head 
    while current:
        count += 1
        if count == k-1:
            current.next = Node(value, current.next)
            break
        current = current.next
    return head 

# insert element before value x (guaranteed that x is present)
def insert_node_before_x(head, value, x):
    if head.data ==x :
        return Node(value, head)
    current = head
    while current.next: 
        if current.next.data == x:
            current.next = Node(value, current.next)
            break
        current = current.next
    return head 

# if x is not present, insertion wont happen
# if i have to print if x is present or not, use a flag. 

# test
arr = [4, 2, 3, 1, 0, 6]
head = convert_to_linkedlist(arr)
head = insert_node_before_x(head, 10, 4)
print_linkedlist(head)

def delete_head(head):
    if head is None: return None
    head = head.next
    return head 

def delete_end_node(head):
    if head is None or head.next is None: return None
    current = head 
    while current.next.next:
        current = current.next
    current.next = None
    return head

# instead of storing a temp node
# def delete_kth_element(head, k):
#     count = 0
#     if head is None: return None
#     if k == 1: head = head.next
#     else:
#         current = head 
#         while current: 
#             count += 1
#             if count == k-1:
#                 current.next = current.next.next
#             current = current.next
#     return head

# using a temp node
# def delete_kth_element(head, k):
#     if head is None: return None
#     if k == 1: 
#         head = head.next
#         return head 
#     count = 0
#     current = head 
#     prev = None
#     while current:
#         count += 1
#         if count == k:
#             prev.next = prev.next.next
#             break
#         prev = current
#         current = current.next
#     return head 


# delete kth node by value instead of position 
def delete_kth_element(head, value):
    if head is None: return None
    if head.data == value: 
        head = head.next
        return head 
    current = head 
    prev = None
    while current:
        if current.data == value:
            prev.next = prev.next.next
            break
        prev = current        
        current = current.next
    return head

# test
arr = [4, 2, 3, 1, 0, 5]
head = convert_to_linkedlist(arr)
# head = delete_head(head)
# head = delete_end_node(head)
head = delete_kth_element(head, 6)
print_linkedlist(head)

def length_of_linkedlist(head):
    count = 0
    while head:
        head = head.next
        count += 1
    return count

# test
arr = [4, 2, 3, 1, 0, 5]
head = convert_to_linkedlist(arr)
print(arr, "length:", length_of_linkedlist(head))

def search_in_linkedlist(head, target):
    while head:
        if head.data == target: return 1
        head = head.next
    return 0

# test
arr = [4, 2, 3, 1, 0, 5]
head = convert_to_linkedlist(arr)
print(search_in_linkedlist(head, 2))
print(search_in_linkedlist(head ,10))