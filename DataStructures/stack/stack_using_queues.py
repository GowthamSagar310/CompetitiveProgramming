from queue import deque

# stack using two queues
class Stack:
    def __init__(self) -> None:
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.appendleft(x)
        while len(self.q1) != 0:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0

# test
myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack.top()) # returns 3