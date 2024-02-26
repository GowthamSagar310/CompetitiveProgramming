# delete a node in BST

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

root_node = Node(10, Node(9, Node(4, Node(1), Node(5)), None), Node(15, Node(14), Node(18, Node(16), Node(19))))

def print_bst(node):
    if not node: return None
    print_bst(node.left)
    print(node.val, end=' ')
    print_bst(node.right)


def delete_a_node(root_node, target):
    if not root_node: return None    
    curr = root_node 
    if curr.val == target:
        if curr.right:
            curr = curr.right
            new_root = curr
            while curr.left:
                curr = curr.left
            curr.left = root_node.left
            return new_root            
        elif curr.left:
            if curr.left: 
                return curr.left

    else:
        parent_node = curr 
        while True:
            if curr.val > target:
                parent_node = curr
                curr = curr.left
            elif curr.val < target:
                parent_node = curr
                curr = curr.right
            else:
                if curr.right and curr.left:
                    # go to the extreme left of parent_node.right
                    temp_node = curr.right
                    parent_node.right = curr.right
                    while temp_node.left:
                        temp_node = temp_node.left
                    temp_node.left = curr.left
                elif curr.right:
                    parent_node.right = curr.right
                elif curr.left:
                    parent_node.right = curr.left
                else:
                    # absolute leaf node 
                    if parent_node.val > target:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                return root_node
            
root = delete_a_node(root_node, 5)
print_bst(root)