"""
you are given a perfect binary tree where all leaves are on the same level, and every parent has 2 children.  The binary tree has the following definition:

struct Node {
  int val
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node.  If there is no next right node, the next pointer should be set to NULL

Initially, all next pointers are set to NULL

example 1:
root = [1, 2, 3, 4, 5, 6, 7]
output = [1, #, 2, 3, #, 4, 5, 6, 7, #]

example 2:
root = []
output = []

Constraint:
the number of nodes in the trees is in the range(0, 2^12 - 1)
-1000 <= Node.val <= 1000
"""


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

    # get node by level first
    def connect(self, root):
        from collections import deque

        # check whether the root is valid
        if not root:
            return root

        # init a queue for BFS, with only root
        queue = deque([root])

        # a loop for all level
        while queue:
            size = len(queue)

            # a loop for each level
            for i in range(size):

                # pop a node from the front of the queue
                node = queue.popleft()

                # establisg connections with node in the same level
                if i < size - 1:
                    node.next = queue[0]

                # add children, if any, to be back of the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root.PrintTree()


root = TreeNode(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)

print(root.connect(root))
"""
time: O(N)
space: O(N)

"""
