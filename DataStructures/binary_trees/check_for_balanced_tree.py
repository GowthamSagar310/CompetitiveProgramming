# https://leetcode.com/problems/balanced-binary-tree/

def solve(root):
    def recur(node):
        if not node: return 0
        l = recur(node.left)
        if l == -1: return -1
        r = recur(node.right)
        if r == -1: return -1
        if abs(l-r) > 1: return -1
        return 1 + max(l,r)
    return recur(root) != -1