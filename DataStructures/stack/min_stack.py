import sys 
class Pair:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

# pair approach  space O(2n) time O(1)
# class Stack:

#     def __init__(self):
#         self.stack = []
#         self.current_size = 0

#     def push(self, data):
#         if self.current_size == 0:
#             self.stack.append(Pair(data, data))
#         else:
#             if self.stack[-1].y < data:
#                 self.stack.append(Pair(data, self.stack[-1].y))
#             else:
#                 self.stack.append(Pair(data, data))
#         self.current_size += 1

#     def pop(self):
#         if self.current_size == 0: return -1
#         pair = self.stack.pop()
#         self.current_size -= 1
#         return pair.y 
    
#     def top(self):
#         if self.current_size == 0: return -1
#         return self.stack[-1].x

#     def getMin(self):
#         if self.current_size == 0: return -1
#         return self.stack[-1].y


# data < min_value 
# 2 * data < 2 * min_value 
# 2 * data < min_value + min_value 
# 2 * data - min_value < min_value 
# so if the top value is less than the current minimum,
# we can be sure that the top value is modified.
# we need to move back to original value and current_minimum to previous. 
# current_top = 2 * data - prev_min
# current_top = 2 * current_min - prev_min
# prev_min = 2 * current_min - current_top                

# if i just take data - min_value, can i be sure that the top_value 
# will always be less or more than the min_value ? is there a distinctive feature ? NO 

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = 0 # operations are performed on non-empty stack
        self.current_size = 0

    def push(self, data: int) -> None:
        if self.current_size == 0:
            self.stack.append(data)
            self.min_value = data 
        else:
            if data < self.min_value:
                top_value = 2 * (data) - self.min_value
                self.min_value = data
                self.stack.append(top_value)
            else:
                self.stack.append(data)
        self.current_size += 1

    def pop(self) -> None:
        if self.stack[-1] < self.min_value:
            self.min_value = 2 * self.min_value - self.stack[-1]
        del self.stack[-1]
        self.current_size -= 1

    def top(self) -> int:
        if self.stack[-1] < self.min_value: 
            return self.min_value
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_value

    def print_stack(self):
        print(self.stack)

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.print_stack()
print(obj.getMin())




