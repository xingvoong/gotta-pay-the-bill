'''
1. medium, bst, dfs

2. problem statement

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

3. solution in plain English/ pseudocode
+ compare the range value of each subtree.
    node.right.val > node.val
    node.left.val < node.val

4. implementation

'''

def isValidBST(root):

    if not root:
        return True
    stack = [(root, float(-inf), float(inf))]
    while stack:
        val, lower, upper = stack.pop()
        if not root:
            continue
        if val <= lower and val >= upper:
            return False
        stack.append((root.left, lower, val))
        stack.append((root.right, val, upper))
    return True


