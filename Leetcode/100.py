# https://leetcode.com/problems/same-tree/

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right


# check if two trees are same. identical structure and same values. 
# refer Leetcode 101, which is slightly different. 
        
def recur(p, q):
    if not p and not q: return True 
    if not p or not q: return False 
    return (p.val == q.val and recur(p.left, q.left) and recur(p.right, q.right))

