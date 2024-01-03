class Node:
    def __init__(self, data, next_node=None):
        self.data = data 
        self.next_node = next_node

class Queue: 

    def __init__(self):
        self.current_size = 0
        self.head = None
        self.tail = None
    
    def push(self, data):
        if self.current_size == 0:
            self.head = Node(data, None)
            self.tail = Node(data, None)
        else:
            newNode = Node(data, None)
            self.tail.next = newNode 
            self.tail = newNode 
        self.current_size += 1
    
    def pop(self):
        # FIFO --> remove head 
        if self.current_size == 0: return -1
        temp_node = self.head 
        self.head = self.head.next 
        temp_node.next = None
        del temp_node
        # return temp_node.data

    def peek(self):
        if self.current_size == 0: return -1
        return self.head.data 

    def size(self):
        return self.current_size
    
    def is_empty(self):
        return self.current_size == 0