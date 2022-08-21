'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-blanaced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of everynode never differs by more than one

Example 1:

input: nums = [-10, -3, 0, 5, 9]
output: [0, -3, 9, -10, null, 5]
explantation: [0, -10, 5, null, -3, null, 9] is also accepted

example 2:
input: nums = [1, 3]
output: [3, 1]

=> they need to be balance and BST
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

    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if left >  right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder travesal: node => left => right
            node = TreeNode(nums[p])
            node.left = helper(left, p - 1)
            node.right = helper(p + 1, right)

            return node

        return helper(0, len(nums) - 1)

root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

nums = [-10,-3,0,5,9]
print(root.sortedArrayToBST(nums))

'''
Algo:
- Implement helper function helper(left, right), which constructs BST from nums elements between indexes left and right:

- if left > right, then there is no elements available for that subtree.  Return None
- Pick left middle element: p = (left + right) // 2
- Initiate the root: root = TreeNode(nums[p])
- Compute recursively left and right subtrees: root.left = helper(left, p - 1)
- root.right = helper(p+1, right)

return helper(0, len(nums) - 1)

'''
