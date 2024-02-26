def zigzag(root):    

    if not root: return []
    reverse = False
    queue = [root]
    array = [[root.val]]
    while queue:
        temp_array = []
        size = len(queue)
        level_order = []
        while size > 0:
            node = queue[0]
            queue = queue[1:]
            if node.left: 
                queue.append(node.left)
                level_order.append(node.left)
            if node.right: 
                queue.append(node.right)
                level_order.append(node.right)
            size -= 1
        reverse = not reverse
        if reverse:
            for i in range(len(level_order)-1, -1, -1):
                temp_array.append(level_order[i].val)
        else:
            for i in range(len(level_order)):
                temp_array.append(level_order[i].val)
        if temp_array : array.append(temp_array)
    return array

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

root = Node(3, Node(9), Node(20, Node(15), Node(7)))
print(zigzag(root))