# https://leetcode.com/problems/even-odd-tree/description/?envType=daily-question&envId=2024-02-29

# root = [1,10,4,3,null,7,9,12,8,6,null,null,2]

def construct_tree(root):
    queue = [root]
    vals = [root.val]
    level = 0
    while queue:
        s = len(queue)
        if level % 2: 
            if not is_decreasing_and_even(vals):
                return False
        else:
            if not is_increasing_and_odd(vals):
                return False
        for _ in range(s):
            node = queue[0]
            if node.left: 
                queue.append(node.left)
                vals.append(node.left.val)
            if node.right: 
                queue.append(node.right)
                vals.append(node.right.val)
            queue.pop(0)
            vals.pop(0)
        level += 1
    return True 


def is_increasing_and_odd(l):
    if l[0] % 2 == 0: return False
    for i in range(1, len(l)):
        if l[i] % 2 == 0 or l[i] <= l[i-1]:
            return False
    return True 

def is_decreasing_and_even(l):
    if l[0] % 2: return False 
    for i in range(1, len(l)):
        if l[i] % 2 or l[i] >= l[i-1]:
            return False
    return True 

def solve(tree):
    j = 1
    index = 0
    level = 0
    while index < len(tree):
        if level % 2: 
            if not is_decreasing_and_even(tree[index: index+j]):
                return False
        else: 
            if not is_increasing_and_odd(tree[index: index+j]):
                return False
        index += j 
        j *= 2
        level += 1
    return True 

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

# root = [2,12,8,5,9,null,null,18,16]

root = Node(1)

root.left = Node(10)
root.right = Node(4)

root.left.left = Node(3)
root.right.left = Node(7)
root.right.right = Node(9)

root.left.left.left = Node(12)
root.left.left.right = Node(8)
root.right.left.left = Node(6)
root.right.right.right = Node(2)


# root = Node(2)
# root.left = Node(12)
# root.right = Node(8)

# root.left.left = Node(5)
# root.left.right = Node(9)

# root.left.left.left = Node(18)
# root.left.left.right = Node(16)


# print(construct_tree(root))



def bfs(root):
    queue = [root]
    even = True 
    while queue:
        prev = float("-inf") if even else float("inf")
        for _ in range(len(queue)):
            node = queue[0]
            if even: 
                if node.val % 2 == 0 or prev >= node.val:
                    return False 
            else:
                if node.val % 2 == 1 or prev <= node.val:
                    return False
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right) 
            queue.pop(0)
            prev = node.val
        even = not even
    return True 

print(bfs(root))
