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
    print(head)

    # I can convert the list, to an array
    # and then from array to BST, like the ealier problem
    def sortedListToBST(head):
        nums = []
        ptr = head
        while ptr:
            nums.append(ptr.val)
            ptr = ptr.next

        # always pick the middle node as the root
        def sortedArrayToBST(nums):
            def helper(left, right):
                if left > right:
                    return None

                # always pick the left as the middle
                p = (left + right) // 2
                root = TreeNode(nums[p])
                root.left = helper(left, p - 1)
                root.right = helper(p + 1, right)
                return root

            return helper(0, len(nums) - 1)

        return sortedArrayToBST(nums)

    root = sortedListToBST(head)
    root.PrintTree()

'''

let N be the number of nodes in linked list
time:
linked list to array: O(N) time
array to BST: O(N) time
=> O(N) time

space: O(N)

'''