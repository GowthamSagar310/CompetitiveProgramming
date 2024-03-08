# https://leetcode.com/problems/maximum-width-of-binary-tree/

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

def get_distance(temp):
    print(temp)
    temp_mod = [x for x in temp if x is not None]
    if len(temp_mod) < 2: return 0 
    l = 0 
    r = len(temp)-1
    while l < r:
        if l is None: 
            l += 1
        elif r is None: 
            r += 1
        else:
            return (r-l+1)
    return 0

def bfs(root):
    if not root: return 0
    queue = [root]
    m = 0
    while queue:
        temp = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left: 
                queue.append(node.left)
                temp.append(node.left.val)
            else:
                temp.append(None)
            if node.right:
                queue.append(node.right)
                temp.append(node.right.val)
            else:
                temp.append(None)
        m = max(m, get_distance(temp))
    return m 

root = Node(1, Node(3, Node(5, Node(6), None), None), Node(2, None, Node(9, Node(7), None)))

print(bfs(root))