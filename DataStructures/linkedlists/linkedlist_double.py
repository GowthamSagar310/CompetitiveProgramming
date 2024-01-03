class Node:

    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

# array to double linkedlist
def convert_to_linkedlist(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1, len(arr)):
        newNode = Node(arr[i], None, prev)
        prev.next = newNode
        prev = newNode
    return head

def print_linkedlist(head):
    while head.next:
        print(head.data, end=' ')
        head = head.next
    print(head.data, end=' ')
    print("||", end=' ')
    while head:
        print(head.data, end = ' ')
        head = head.prev
    print()

arr = [4, 2, 3, 1, 0, 5]
head = convert_to_linkedlist(arr)
print_linkedlist(head)

def delete_head(head):
    if head is None: return None
    if head.next is None: return None
    temp = head
    head = head.next
    head.prev = None
    temp.next = None
    return head

def delete_tail(head):
    if head is None: return None
    if head.next is None: return None
    temp = head
    while temp.next:
        temp = temp.next
    previous = temp.prev
    temp.prev = None
    previous.next = None
    return head


arr = [4, 2, 3, 1, 0, 5]
head = convert_to_linkedlist(arr)
print_linkedlist(head )
