"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it too a height balanced BST

For this problem, a height-balanced binary tree is defined as binary tree in which the depth of the two subtrees of every node never differ by more than 1

example 1:
Input: head = [-10, -3, 0, 5, 9]
Output: [0, -3, 9, -10, null, 5]

example 2:
input: head = []
output: []

constraints:
- the number of nodes in head is in the range [0, 2 * 10^4]
- -10^5 <= node.val <= 10^5


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


# Node class
class ListNode:

    # funtion to init the node object
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):

        # defining a blank result variable
        result = ""

        # initializing ptr to head
        ptr = self

        # traversing and adding it to res
        while ptr:
            result += str(ptr.val) + ", "
            ptr = ptr.next
        # remove trainling commas and white space
        result = result.strip(", ")

        if len(result):
            return "[" + result + "]"
        else:
            return result


# Code execution
if __name__ == "__main__":
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    head.next = node1
    node1.next = node2
    #print(head)

    # I can convert the list, to an array
    # and then from array to BST, like the ealier problem
    def getSize(head):
      size = 0
      ptr = head
      while ptr:
        size += 1
        ptr = ptr.next

      return size

    def sortedListToBST(head):

      # get the size so I can find the middle
      size = getSize(head)

      # construct a BST base on preorder
      def helper(left, right):
        nonlocal head
        # print("hello?")
        # print("left", left)
        # print("right", right)
        if left > right:
          return None

        # get the middle
        mid = (left + right) // 2

        # # preorder traversal: node, left, right
        # root = TreeNode(head.val)
        # head = head.next

        # root.left = helper(left, mid - 1)
        # root.right = helper(mid + 1, right)

        #inorder: left, node, right
        left = helper(left, mid - 1)

        root = TreeNode(head.val)
        # need to move the head
        head = head.next

        root.left = left

        right = helper(mid + 1, right)
        root.right = right

        return root

      return helper(0, size - 1)

    root = sortedListToBST(head)
    root.PrintTree()

    #print(sortedListToBST(head))

'''

let N be the number of nodes in linked list

time: O(N)

space: O(log(N)) for recursive stack, the height of the tree

'''