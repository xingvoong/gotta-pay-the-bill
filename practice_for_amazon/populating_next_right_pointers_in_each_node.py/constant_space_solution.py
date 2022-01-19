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
        if not root:
            return root

        # start with the root node.  There are no next pointers
        # that need to be set up on the first level
        leftmost = root

        # once we reach the final level, we are done
        while leftmost.left:
            # iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level
            head = leftmost
            while head:

                # connection 1, 2 nodes share the same parent
                head.left.next = head.right

                # connection 2, between 2 nodes with different parents
                if head.next:
                    head.right.next = head.next.left

                # progress along the current level, aka, the list:
                head = head.next

            # move to the next level:
            leftmost = leftmost.left

        return root


root = TreeNode(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)

print(root.connect(root))
"""
Let N be the number of nodes
- Time: O(N)
- Space: O(1)

"""
