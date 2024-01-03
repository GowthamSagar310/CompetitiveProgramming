class Stack:

    def __init__(self, max_size):
        self.stack = []
        self.pointer = -1
        self.max_size = max_size
        self.current_size = 0

    def push(self, val):
        if self.current_size == self.max_size:
            print("stack full")
            return
            # either return None / -1 or raise some error
        self.stack.append(val)
        self.pointer += 1
        self.current_size += 1
    
    def top(self):
        if self.current_size == 0:
            return ("stack empty") 
            # either return None / -1 or raise some error
        return self.stack[self.pointer]
    
    def pop(self):
        if self.current_size == 0: 
            return ("stack empty")
            # either return None / -1 or raise some error
        value = self.stack[-1]
        del self.stack[-1]
        self.pointer -= 1
        self.current_size -= 1
        return value 

    def print_stack(self):
        print(self.stack, self.current_size)

    def print_pointer(self):
        print(self.pointer)

# test 

stack = Stack(2)
stack.push(2)
stack.push(3)
print(stack.top()) # 3 
print(stack.pop()) # 3
print(stack.top()) # 2 
stack.print_stack()
stack.push(1)
stack.push(3) 
stack.print_stack()
print(stack.pop())
print(stack.pop())
print(stack.top())
print(stack.pop())
stack.push(3)
stack.push(5)
print(stack.pop())
print(stack.pop())
