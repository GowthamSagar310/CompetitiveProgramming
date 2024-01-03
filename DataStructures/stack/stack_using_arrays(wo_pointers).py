# stack using two lists (without pointers)
class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q2.append(x)
        for i in self.q1:
            self.q2.append(i)
        self.q1 = []
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack.top()) # returns 3