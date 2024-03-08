class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

root = Node(5, Node(4, Node(11, Node(7), Node(2))), Node(8, Node(13), Node(4, Node(5), Node(1))))

# given that all values are unique.
def root_to_some_leafnode(node, targetnode, ds, ans):
    if not node: return 
    if not node.left and not node.right:
        if node.val == targetnode.val:
            ans.append(ds.copy() + [targetnode.val])
    
    ds.append(node.val)
    root_to_some_leafnode(node.left, targetnode, ds, ans)
    root_to_some_leafnode(node.right, targetnode, ds, ans)
    ds.pop()

ds = []
ans = []
root_to_some_leafnode(root, Node(2), ds, ans)
print(ans)

def all_paths(node, ds, ans):
    if not node: return 
    if not node.left and not node.right:
        ans.append(ds.copy() + [node.val])
    
    ds.append(node.val)
    all_paths(node.left, ds, ans)
    all_paths(node.right, ds, ans)
    ds.pop()

ds, ans = [], []
all_paths(root, ds, ans)
print(ans)

# given that all values are unique.
def root_to_any_node(node, target, ans):
    if not node: return False 
    ans.append(node.val)
    if node.val == target:
        return True 
    if root_to_any_node(node.left, target, ans) or root_to_any_node(node.right, target, ans):
        return True 
    ans.pop()
    return False 

ds, ans = [], []
root_to_any_node(root, 13, ans)
print(ans)
