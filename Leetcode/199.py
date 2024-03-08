# https://leetcode.com/problems/binary-tree-right-side-view/description/


def bfs(root):
    if not root: return []
    queue = [root]
    ans = []
    while queue:
        ans.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return ans 


       # root,    0,    []
def dfs(root, level, result):
    if not root: return 
    if level == len(result):
        result.append(root.val)
    dfs(root.right, level+1, result) # observe that right is being called first. 
    dfs(root.left, level+1, result)

