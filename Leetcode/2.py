# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next


def addTwoNumbers(l1, l2):
    node1 = l1
    node2 = l2 
    carry = 0
    head = ListNode(node1.val)
    temp = head 
    while node1 and node2:
        value = node1.val + node2.val + carry
        carry = value // 10
        value = value % 10
        newNode = ListNode(value)
        temp.next = newNode
        temp = newNode
        node1 = node1.next
        node2 = node2.next

    while node1:
        value = node1.val + carry
        carry = value // 10
        value = value % 10

        newNode = ListNode(value)
        temp.next = newNode
        temp = newNode

        node1 = node1.next

    while node2:
        value = node2.val + carry
        carry = value // 10
        value = value % 10
        
        newNode = ListNode(value)
        temp.next = newNode
        temp = newNode

        node2 = node2.next

    if carry == 1:
        newNode = ListNode(carry)
        temp.next = newNode 
    
    return head.next



arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def convert_to_ll(arr):
    head = ListNode(arr[0])
    temp = head 
    for i in range(1,len(arr)):
        newNode = ListNode(arr[i])
        temp.next = newNode
        temp = newNode
    return head 

def print_ll(head):
    temp = head 
    while head:
        print(head.val, end=" ")
        head = head.next
    return temp

h1 = convert_to_ll(arr1)
h2 = convert_to_ll(arr2)

print_ll(addTwoNumbers(h1,h2))