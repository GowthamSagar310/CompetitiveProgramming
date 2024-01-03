class Queue:

    # because i need to remove elements from top
    # i need a separate pointer that points to it.

    def __init__(self, max_size):
        self.queue = [-1] * max_size
        # ----------
        # |---last--|
        # |---------|
        # |---------|
        # |--first--| -> always get this element first. 
        # -----------

        # initial config
        self.first = -1
        self.last = -1
        self.current_size = 0
        self.max_size = max_size
        
    
    def push(self, val):

        if self.current_size == self.max_size:
            print("queue full")
            return 
        
        # if initial config 
        if self.last == -1: # bottom = -1 only initially
            self.last = 0 
            self.first = 0
        else:
            self.last = (self.last + 1) % self.max_size # circular
        
        # append wont work. so i need a arr with default vals before hand. 
        self.queue[self.last] = val 
        self.current_size += 1
    
    def pop(self):

        if self.current_size == 0:
            return "queue empty"

        val = self.queue[self.first]

        if self.current_size == 1:
            self.first = -1
            self.last = -1
        else:
            self.first = (self.first + 1) % self.max_size    
    
        # do not use delete because the push is going replace the values 
        # del self.queue[self.first]
        self.current_size -= 1
        return val 


    def top(self):
        if self.current_size == 0:
            return "queue empty"
        return self.queue[self.first]

    def size(self):
        return self.current_size
    

# test
queue = Queue(5)
queue.push(2)
queue.push(3)
queue.push(1)
queue.push(4)
print(queue.top())
print(queue.size())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.size())
queue.push(3)
queue.push(1)
queue.push(4)
print(queue.top())
