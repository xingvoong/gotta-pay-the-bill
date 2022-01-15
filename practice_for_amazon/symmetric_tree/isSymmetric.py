'''
Given the root of binary tree, check whether it is a mirror of itself (i.em symetric around it center)

Constraints:

- the number of nodes in the tress is in the range [1, 1000].
- -100 <= node.val <= 100
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

    def isSymmetric(self, root):

      def isMirror(root1, root2):
        if not root1 and not root1:
          return True
        if not root1 or not root2:
          print("root1", root1)
          print("root2", root2)
          return False

        print("root1.value", root1.value)
        print("root2.value", root2.value)

        return ((root1.value == root2.value) and
                isMirror(root1.right, root2.left) and
                isMirror(root1.left, root2.right))

      return isMirror(root, root)




root = TreeNode(1)
root.insert(2)
root.insert(2)
# root.insert(3)
# root.insert(4)
# root.insert(4)
# root.insert(3)

print(root.inorderTraversal(root))
print(root.isSymmetric(root))