# binary tree 

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

graph = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["F"]
}

root_node = Node("A")
root_node.left = Node("B")
root_node.right = Node("C")
root_node.left.left = Node("D")
root_node.left.right = Node("E")
root_node.right.left = Node("F")

def walk(node):
    if node is not None:
        print(node.value)
        walk(node.left)
        walk(node.right)

def walk_stack(root_node):
    stack = []
    stack.append(root_node)
    while stack:
        node = stack.pop()
        if node is not None:
            print(node.value)
            stack.append(node.right)
            stack.append(node.left)

def search(root_node, target):
    if root_node is None: return None
    if root_node.value == target: return root_node
    return search(root_node.left,target) or search(root_node.right, target)

print(search(root_node, "B").value)