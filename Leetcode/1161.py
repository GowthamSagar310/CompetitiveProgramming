
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

root = Node(1)

def solve(root):
    level = 1
    queue = [root]
    maxsum = float("-inf")
    minlevel = float("-inf")
    while queue:
        current_sum = sum([node.val for node in queue])
        if current_sum > maxsum:
            maxsum = current_sum
            minlevel = max(minlevel, level)
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        level += 1
    return minlevel

print(solve(root))