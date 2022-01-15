'''
Given the roots of 2 binary trees p and q, write a function to check if they are the same or not. Solve this recursively

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value

Example:
input:
p = [1, 2, 3]
q = [1, 2, 3]

Output: true

input: p = [1, 2], q = [1, null, 2]
output: false

input: p = [1, 2, 1], q = [1, 1, 2]
output: false

- the number of nodes in both trees is in the range [0, 100]
- -10^4 <= Node.val <= 10^4
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

    def isSameTree(self, p, q):

      from collections import deque

      def check(p, q):

        if not p and not q:
          return True

        if not p or not q:
          return False

        if p.value != q.value:
          return False

        return True
      # make a queue
      # add node into it and then check the node with a helper function
      # helper function check whether those 2 nodes are valid for the tree to be the same
      queue = deque([(p, q)])

      while queue:
        p, q = queue.popleft()

        if not check(p, q):
          return False

        if p:
          queue.append((p.left, q.left))
          queue.append((p.right, q.right))

      return True


p = TreeNode(1)
p.insert(2)
p.insert(3)

q = TreeNode(1)
q.insert(2)
q.insert(3)

print(p.isSameTree(p, q))



'''
# start from the root and then at each iteration pop the current node out of the dequeu.  Then do the same checks as in the approach 1:
- p and q are not None
- p.val is equal to q.val

and if checks are ok, push the child nodes

'''