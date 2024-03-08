# recursive
def get_max_depth(node):
    if not node: return 0 
    l = get_max_depth(node.left)
    r = get_max_depth(node.right)
    return 1 + max(l, r)

def max_depth_iterative(root_node):
    if not root_node: return 0
    queue = [root_node]
    level = 0
    while queue:
        size = len(queue)
        while size > 0:
            node = queue[0]
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            queue = queue[1:]
            size -= 1
        level += 1
    return level

# testing

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = right

"""
        1
    2       3
  4   5   6   7
"""
bt1_root_node = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

"""
    1
      2
        3
          4
        6   5 
"""
bt2_root_node = Node(1, None, Node(2, None, Node(3, None, Node(4, Node(6), Node(5)))))

"""
          1
      2       3
    4   5   6    7
  8            10
9             11
"""

bt3_root_node = Node(1, Node(2, Node(4, Node(8, Node(9))), Node(5)), Node(3, Node(6), Node(7, Node(10, Node(11)))))

print(max_depth_iterative(bt1_root_node))
print(max_depth_iterative(bt2_root_node))
print(max_depth_iterative(bt3_root_node))
