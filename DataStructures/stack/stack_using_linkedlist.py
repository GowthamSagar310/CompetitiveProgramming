class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:

    def __init__(self):
        self.current_size = 0 
        self.head = None

    def getSize(self):
        return self.current_size 

    def isEmpty(self):
        return self.current_size == 0

    def push(self, data):
        newNode = Node(data, self.head)
        self.head = newNode 
        self.current_size += 1

    def pop(self):
        if not self.head: return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        del temp
        self.current_size -= 1


    def getTop(self):
        if self.current_size == 0: return -1
        return self.head.data
        