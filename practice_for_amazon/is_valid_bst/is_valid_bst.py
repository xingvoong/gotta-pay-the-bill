'''
Given the root of a binary tree, determine if it is a valid binart search tree (BST).

A valid BST is defined as follows:
- the left subtree of a node contains only nodes with keys less than the node's key.
- the right subtree of a node contains only node with key greater tha the node's key.
- both the left and right subtrees must also be binary search trees.

input: root = [2, 1, 3]
output: true

'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # insert into a binary tree
    # recursively go to the leaf so that I can add something.
    def insert(self, value):
        # if the node is there with a value already
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)
        # if the node is there but with no value
        else:
            self.value = value

    # print tree
    # visit the left
    # print the node val
    # visit the right
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()

    # in-order traversal, left, node, right
    # create an empty list,
    # add left node first followed by the root or parent node

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.value)
            res += self.inorderTraversal(root.right)
        return res

    # pre-order traversal, node, left right

    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.value)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res

    # post-orde traversal, left, right, node
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.value)
        return res

    def isValidBST(self, root):
      import math
      def validate(root, low = -math.inf, high = math.inf):

        # empty trees are valid BSTs
        if not root:
          return True

        # current node must be between low and high
        if root.value <= low or root.value >= high:
          return False

        # the left and right subtree must also be valid.
        return (validate(root.right, root.value, high) and
                validate(root.left, low, root.value))

      return validate(root)

root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

root1 = TreeNode(2)
root1.insert(1)
root1.insert(3)

print(root.isValidBST(root))

'''
time: O(N), we visit each node once

space: O(N), for recursive stack

Key take away:
- have a lower and upper limit depends on where you are.
- every substree need to be a BST as well
'''



