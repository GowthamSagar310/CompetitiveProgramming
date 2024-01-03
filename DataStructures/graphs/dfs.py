# binary tree 

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

# root_node = Node("A")
# root_node.left = Node("B")
# root_node.right = Node("C")
# root_node.left.left = Node("D")
# root_node.left.right = Node("E")
# root_node.right.left = Node("F")

# first time, when this is ran, it would be on the root-node of whole tree 
# or if you have access to some node, and then want to walk from there. 

# this variation returns None at the end
def walk(node):
    if node is None: return None
    print(node.data)
    return walk(node.left) or walk(node.right)

# this returns nothing
def walk(node):
    if node is None: return
    print(node.data)
    walk(node.left) 
    walk(node.right)

# this returns nothing
def walk_stack(node):
    stack = []
    stack.append(node)
    while stack:
        n = stack.pop()
        if n is not None:
            # the order of addition into the stack, determines my traversal order
            stack.append(n.right)
            stack.append(n.left)
            print(n.data)

def search(node, target):
    # use return statements to take data back to the parent
    if node is None: return None
    if node.data == target: return node.data
    left = search(node.left, target)
    # if left is None, then check for right 
    # if left is not None, back propagate the target to the parent. 
    if left is not None: 
        return left
    return search(node.right, target)
    

# print data folder
def print_structure(node, indentation):
    if node is None: return
    print(" " * indentation + "|-" + node.data)
    print_structure(node.left, indentation+2)
    print_structure(node.right, indentation+2)

# print_structure(root_node, 0)

# maximum in a binary tree
# root_node = Node(5)
# root_node.left = Node(4)
# root_node.right = Node(6)
# root_node.left.left = Node(3)
# root_node.left.right = Node(8)
# root_node.left.right.right = Node(6)
# root_node.left.right.right.right = Node(10)
# root_node.right.left = Node(7)

def get_max(node):
    if node is None: return -1  # assuming values are >= 0
    return max(node.data, get_max(node.left), get_max(node.right))

# max depth (number of edges in the path)

def max_depth(node):
    if node is None: return -1
    return max(1 + max_depth(node.left), 1 + max_depth(node.right))

# number of visible nodes 
# how many number of nodes (inclusive) from in the path of root to the node 
# are strictly greater than node.data

def visible_nodes(node, current_max):
    if node is None: return 0
    count = 0
    if node.data > current_max:
        count += 1
        current_max = node.data
    count += visible_nodes(node.left, current_max) + visible_nodes(node.right, current_max)
    return count

root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
root_node.left.left = Node(4)
root_node.left.right = Node(5)
root_node.left.left.right = Node(7)
root_node.right.right = Node(6)
# root_node.right.right.left = Node(8)

def balanced_tree(node):
    if node is None: return 0
    l_depth = 1 + balanced_tree(node.left)
    r_depth = 1 + balanced_tree(node.right)
    if abs(l_depth - r_depth) > 1:
        return -1
    return max(l_depth, r_depth)

print(balanced_tree(root_node))