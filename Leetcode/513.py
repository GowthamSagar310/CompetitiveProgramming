# https://leetcode.com/problems/find-bottom-left-tree-value/
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(3)
root.right.left = Node(5)
root.right.left.left = Node(7)
root.right.right = Node(6)

def bfs(root_node):
    queue = [root_node]
    left_most = root_node.val
    while queue:
        s = len(queue)
        left_most = queue[0].val
        for _ in range(s):
            node = queue[0]
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
            queue.pop(0)
    return left_most

print(bfs(root))