from queue import LifoQueue

class MyQueue:

    def __init__(self) -> None:
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()

    def push(self, x):

        # self.s1 should be in correct order
        while not self.s1.empty():
            self.s2.put(self.s1.get())
        
        self.s2.put(x)

        while not self.s2.empty():
            self.s1.put(self.s2.get())

    def pop(self):
        return self.s1.get()

    def top(self):
        return self.s1.queue[-1]
    
    def size(self):
        return self.s1.qsize()



queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.print_queue()
queue.get()
queue.get()