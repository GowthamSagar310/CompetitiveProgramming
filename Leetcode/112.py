# https://leetcode.com/problems/path-sum/

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

root = Node(5, Node(4, Node(11, Node(7), Node(2))), Node(8, Node(13), Node(4, None, Node(1))))

def recur(node, target):
    if not node: return False 
    if not node.left and not node.right:
        if target-node.val == 0:
            return True 
        return False
    left, right = False, False
    if node.left:
        left = recur(node.left, target-node.val)
    if node.right:
        right = recur(node.right, target-node.val)
    return left or right

print(recur(root, 22))


        
