# binary tree traversals 

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

# ========================================================
# PRE-ORDER 
# Root Left Right
def pre_order_recursive(node, array):
    if not node: return
    array.append(node.val)
    pre_order_recursive(node.left, array)
    pre_order_recursive(node.right, array)
    return array

def pre_order_iterative(root_node):
    curr, stack, array = root_node, [], []
    while curr or stack:
        if curr:
            array.append(curr.val)
            if curr.right: stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()
    return array

# ========================================================
# IN-ORDER  
# Left Root Right

def in_order_recursive(node, array):
    if not node: return 
    in_order_recursive(node.left, array)
    array.append(node.val)
    in_order_recursive(node.right, array)
    return array

def in_order_iterative(root_node):
    curr, stack, array = root_node, [], []    
    while curr or stack:
        if curr:
            stack.append(curr)            
            curr = curr.left
        else:
            curr = stack.pop()
            array.append(curr.val)
            curr = curr.right
    return array

# ========================================================
# POST-ORDER  
# left right root

def post_order_recursive(node, array):
    if not node: return 
    post_order_recursive(node.left, array)
    post_order_recursive(node.right, array)
    array.append(node.val)
    return array

def post_order_iterative(root_node):
    curr, stack, array = root_node, [], []

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # it only comes here if not left is present.
            # so, check if right is present
            temp = stack[-1].right
            if temp:
                # if yes, explore right
                curr = temp
            else:
                # if no, then its time to process root. 
                # but what if this temp node is, its parent's right ? 
                # then we can process its parent too. 
                temp = stack.pop()
                array.append(temp.val)
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    array.append(temp.val)

    return array

# the idea is to go from reverse
# post order --> LEFT RIGHT ROOT 
# so root is the one, that is last to be seen
# so root must be seen at the last, then the right, then the left
# if root must be seen last, it must be added first to the stack.
def post_order_two_stacks(root_node):
    s1 = []
    s2 = []
    array = []
    s1.append(root_node)
    while s1:
        node = s1.pop()
        s2.append(node)
        # next left must be added to s1, and then right 
        # so that, in s2, right will the be one going next.
        if node.left: s1.append(node.left)
        if node.right: s1.append(node.right)
    while s2:
        array.append(s2.pop().val)
    return array

# =================================================
# all traversals at a time 

def all_traversals(root_node):
    pre_order, in_order, post_order = [], [], []
    stack = [(root_node, 1)]
    
    while stack:
        node, rep = stack.pop()
        if rep == 1:
            # this is the first time, i am seeing this node
            # this must be in pre-order
            pre_order.append(node.val)
            # but in-order, post-orders need me 
            stack.append((node, 2))
            # i need to move left
            if node.left: stack.append((node.left, 1))
            # what about my right side ?
            # that i ll take care when i come back
        elif rep == 2:
            # my left side is done, so i came back
            in_order.append(node.val)
            # may be post_order needs me 
            stack.append((node, 3))
            # what about my right side ? so first i ll process my right side and then come back
            if node.right: stack.append((node.right, 1))
        else:
            # my left is done
            # my right is done 
            # i must be post order
            post_order.append(node.val)
    
    return pre_order, in_order, post_order

# testing 

# print("inorder traversals")
# print(in_order_recursive(bt1_root_node, []))
# print(in_order_iterative(bt1_root_node))

# print(in_order_recursive(bt2_root_node, []))
# print(in_order_iterative(bt2_root_node))

# print(in_order_recursive(bt3_root_node, []))
# print(in_order_iterative(bt3_root_node))


# print("preorder traversals")
# print(pre_order_recursive(bt1_root_node, []))
# print(pre_order_iterative(bt1_root_node))

# print(pre_order_recursive(bt2_root_node, []))
# print(pre_order_iterative(bt2_root_node))

# print(pre_order_recursive(bt3_root_node, []))
# print(pre_order_iterative(bt3_root_node))

# print("postorder traversals")
# print(post_order_recursive(bt1_root_node, []))
# print(post_order_iterative(bt1_root_node))
# print(post_order_two_stacks(bt1_root_node))

# print(post_order_recursive(bt2_root_node, []))
# print(post_order_iterative(bt2_root_node))
# print(post_order_two_stacks(bt2_root_node))

# print(post_order_recursive(bt3_root_node, []))
# print(post_order_iterative(bt3_root_node))
# print(post_order_two_stacks(bt3_root_node))

print(all_traversals(bt1_root_node))
