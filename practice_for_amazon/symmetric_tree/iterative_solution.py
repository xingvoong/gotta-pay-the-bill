"""
Given the root of a binary tree, check whether it is mirror of itself (i.e symmetric around its center)

Input: root = [1, 2, 2, 3, 4, 4, 3]
Output:

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

    def isSymmetric(self, root):
        from collections import deque

        queue = deque()
        queue.append(root)
        queue.append(root)
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()

            if not t1 and not t2:
                continue

            if not t1 or not t2:
                return False

            if t1.value != t2.value:
                return False

            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)

        return True


root = TreeNode(1)
root.insert(2)
root.insert(2)
# root.insert(3)
# root.insert(4)
# root.insert(4)
# root.insert(3)

# print(root.inorderTraversal(root))
print(root.isSymmetric(root))


"""
Instead of recursion, we can also use iteration with the aid of queue.   Each two consecutive nodes in the queue should be equal, and their subtrees a mirror of each other.  Initially, the queue contrains root and root.  then the algo works similarly to BFS, with some key differences.  Each time, 2 nodes are extracted and their values compared.  Then the right and left children of the 2 nodes are inserted in the queue in opposite order. The algo is done when either the queue is empty, or we detect that the tree is not symmetric (i.e we pull out 2 consecutive nodes from the queue that are unequal)

"""
