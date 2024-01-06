class BinaryHeap:
    # uses 1-based indexing 

    # initial config [0] len 0
    # intermediate   [0,10,8,9,6,7,8,9] len 7
    #                    1 2 3 4 5 6 7  
    #                    1 --> 2,3 (2*i, 2*i+1) children 
    #                    2 --> 4,5 (2*i, 2*i+1) children
    #                    5 --> (2*i // 2) or ((2*i+1) // 2) --> i --> 2 
    # if i used 0 based indexing, children would be 2*i+1 2*i+2
    # and to find parent it would have been confusing, to decide if its left child or right child
     

    def __init__(self) -> None:
        self.items = [0]
    
    def __len__(self):
        return len(self.items)-1
    
    def push(self, value):
        self.items.append(value)
        self.percolate_up(len(self))
    
    def percolate_up(self, i):
        # if parent has less value, then move up 
        # first element is 1, cant move up than this 
        while i // 2 > 0:
            if self.items[i] > self.items[i//2]:
                self.items[i], self.items[i//2] = self.items[i//2], self.items[i]
            i = i // 2 # move to parent
    
    def pop(self):
        if self.is_empty(): return -1
        return_value = self.items[1]
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        del self.items[-1]
        self.percolate_down(1)
        return return_value

    def percolate_down(self, i):
        # if 2 * i <= len(self) then 2 * i child is present. 
        # [0,1,2] 
        # i=1, 2*i = 2, len(self) = 2, 2 <= 2
        while 2*i <= len(self): 
            max_child_index = self.max_child(i)
            if self.items[max_child_index] > self.items[i]:
                self.items[i], self.items[max_child_index] = self.items[max_child_index], self.items[i]
            i = max_child_index

    def max_child(self, i):
        # i is the parent 
        # 2*i and 2*i+1 are the children
        if 2*i+1 > len(self):
            return 2*i
        if self.items[2*i] > self.items[2*i+1]:
            return 2*i
        return 2*i+1

    def delete(self, index):
        if not self.is_empty() and index > 0 and index <= len(self):
            self.items[index], self.items[-1] = self.items[-1], self.items[index]
            temp = self.items[index]
            self.percolate_down(index)
            if self.items[index] == temp:
                self.percolate_up(index)
            # self.percolate_down(index)
            # self.percolate_up(index)
            


    def peek(self):
        if self.is_empty(): return -1
        return self.items[1]

    def size(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0

    def __repr__(self):
        return str(self.items)

class BinaryHeapMin:

    def __init__(self) -> None:
        self.items = [0]

    def __len__(self):
        return len(self.items)-1

    def push(self,value):
        self.items.append(value)
        self.percolate_up(len(self))
    
    def percolate_up(self, i):
        # if child has lesser element than parent, move up.
        while i // 2 > 0:
            if self.items[i] < self.items[i//2]:
                self.items[i], self.items[i//2] = self.items[i//2], self.items[i]
            i = i // 2

    def pop(self):
        if self.is_empty(): return -1
        return_value = self.items[1]
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        self.items.pop()
        self.percolate_down(1)
        return return_value

    def percolate_down(self,i):
        while 2*i <= len(self):
            min_child_index = self.min_child(i)
            if self.items[min_child_index] < self.items[i]:
                self.items[min_child_index], self.items[i] = self.items[i], self.items[min_child_index]
            i = min_child_index 
           
    def min_child(self, i):
        if 2*i+1 > len(self):
            return 2*i
        if self.items[2*i] < self.items[2*i+1]:
            return 2*i
        return 2*i+1

    def delete(self, index):
        if not self.is_empty() and index > 0 and index <= len(self):
            self.items[index], self.items[-1] = self.items[-1], self.items[index]
            temp = self.items[index]
            self.percolate_down(index)
            if self.items[index] == temp:
                self.percolate_up(index)
            # either one thing happens
            # self.percolate_down(index)
            # self.percolate_up(index)
            
    def peek(self):
        if self.is_empty(): return -1
        return self.items[1]

    def size(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0

    def __repr__(self):
        return str(self.items)

bh = BinaryHeapMin()
for _ in range(int(input())):
    query = input()
    if len(query.split()) > 1:
        option, value = list(map(int, query.split()))
        if option == 2:
            bh.push(value)
    else:
        print(bh.pop(), end=" ")

# bh = BinaryHeapMin()
# bh.push(17)
# bh.push(7)
# bh.push(18)
# print(bh)
# print(bh.pop())
# print(bh)

# testing.
# bh = BinaryHeap()
# bh = BinaryHeapMin()
# bh.push(11)
# bh.push(10)
# bh.push(8)
# bh.push(9)
# bh.push(8)
# print(bh)
# print(bh.peek())
# print(bh.size())
# print(bh.pop())
# print(bh.pop())
# print(bh)
# bh.push(10)
# print(bh)
# bh.push(1)
# bh.push(2)
# bh.push(3)
# print(bh)
# print(bh.pop())
# print(bh)
# print(bh.pop())
# print(bh.pop())
# print(bh.pop())
# print(bh)

# bh = BinaryHeapMin()
# bh.push(2)
# bh.push(1)
# print(bh.pop())