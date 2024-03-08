# https://leetcode.com/problems/count-complete-tree-nodes/

# normal approach would be O(N)
# 
# def solve(root):
#     ans  = 0
#     if not root: return 0
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         ans += 1
#         if node.left: stack.append(node.left)
#         if node.right: stack.append(node.right)
#     return ans
# 
# but they mentioned its a complete binary tree. so we can optimize it.

def get_left_height(root):
    c = 0
    while root:
        c += 1
        root = root.left 
    return c 

def get_right_height(root):
    c = 0
    while root:
        c += 1
        root = root.right 
    return c 


def solve(root):
    if not root: return 0

    lh = get_left_height(root)
    rh = get_right_height(root)

    # left most and right most are filled. so we can simply calculate number of nodes.
    if lh == rh: 
        return (1 << lh) - 1

    return 1 + solve(root.left) + solve(root.right)
