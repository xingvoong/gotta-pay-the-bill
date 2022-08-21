'''
Given the root of binary tree, return the level order traversal of its node's values (i.e from left to right, level by level)

Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]

Example 2:
input: root = [1]
output: [[1]]

Example 3:
input: root = []
output: []

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

    def levelOrder(self, root):
      from collections import deque
      # return result
      result = []

      # check whether the input is valid
      if not root:
        return root


      level = 0
      # queue for BFS
      queue = deque([root])

      # process the queue (or all the level)
      while queue:
        # open the level
        result.append([])

        # number of elements in the current level
        num = len(queue)

        # process the current level
        for i in range(num):
          node = popleft()

          result[level].append(node.value)
          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)

        level += 1

      return levels



root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# print("inorderTraversal", root.inorderTraversal(root))
# print("preorderTraversal", root.preorderTraversal(root))
# print("postorderTraversal", root.postorderTraversal(root))

print(root.levelOrder(root))


'''
time:
let N be the number of nodes in the tree
time: O(N), the time to call helper
space: O(N), for recursive stack


take aways:
- Have the result as return value
- if len(result) == level: we append spot for that level's node.
- travel left and right with increasing level.
'''
