# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

from collections import defaultdict


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

root = Node(3, Node(5, Node(6), Node(2, Node(7), Node(4))), Node(1, Node(0), Node(8)))

ans = []
target = 5
k = 2

# better use defaultdict 
def create_graph(node):
    adj = defaultdict(list)
    queue = [node]
    while queue:
        node = queue.pop(0)
        if node.left: 
            queue.append(node.left)
            adj[node.val].append(node.left.val)
            adj[node.left.val].append(node.val)
        if node.right: 
            queue.append(node.right)
            adj[node.val].append(node.right.val)
            adj[node.right.val].append(node.val)
    return adj

adj = create_graph(root)
def bfs(adj, target, k):
    if k == 0: return [target.val] # this is can done at first
    queue = [target]
    ans = []
    c = 0
    visited = []
    while queue:
        c += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            visited.append(node)
            for nn in adj[node]:
                if nn not in visited:
                    if c == k:
                        ans.append(nn)
                    queue.append(nn)
    return ans 


print(bfs(adj, target, k))