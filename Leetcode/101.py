# https://leetcode.com/problems/symmetric-tree/description/

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

root = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))


def recur(left, right):
    if not left and not right:
        return True 
    if not left or not right:
        return False 
    return (left.val == right.val and recur(left.left, right.right) and recur(left.right, right.left))

# handle if root itself is None. 
print(recur(root.left, root.right))