# https://leetcode.com/problems/minimum-depth-of-binary-tree/

root = [3,9,20,None,None,15,7]
root = [2,None,3,None,4,None,5,None,6]

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

root = Node(2)
root.right = Node(3)
root.right.right = Node(4)
root.right.right.right = Node(5)
root.right.right.right.right = Node(6)

def recur(node):
    if not node: return 0 
    if not node.left: return recur(node.right) + 1
    if not node.right: return recur(node.left) + 1
    return min(recur(node.left), recur(node.right)) + 1

print(recur(root))