# https://leetcode.com/problems/path-sum-ii/description/

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

root = Node(5, Node(4, Node(11, Node(7), Node(2))), Node(8, Node(13), Node(4, Node(5), Node(1))))


def recur(node, targetsum, ds, ans):
    if not node: return []
    if not node.left and not node.right:
        if targetsum-node.val==0:
            ans.append([node.val] + ds.copy())
    ds.append(node.val)
    recur(node.left, targetsum-node.val, ds, ans)
    recur(node.right, targetsum-node.val, ds, ans)
    ds.pop()

ans = []
ds = []
recur(root, 22, ds, ans)
print(ans)            
