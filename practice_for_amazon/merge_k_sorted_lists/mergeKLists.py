'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascesding order

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
O: [1, 1, 2, 3, 4, 4, 5, 6]
Explanation: the linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into on sorted list:
1->1->2->3->4->4->5->6

Example 2:
I: lists = []
O: []

Example 3:
I: lists = [[]]
O: []

'''
# Node class
class ListNode:

  # funtion to init the node object
  def __init__(self, val, next = None):
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
      return []


# Code execution
if __name__ == '__main__':

  # a linked list
  node11 = ListNode(1)
  node12 = ListNode(4)
  node13 = ListNode(5)
  node11.next = node12
  node12.next = node13

  # another linked list
  node21 = ListNode(1)
  node22 = ListNode(3)
  node23 = ListNode(4)
  node21.next = node22
  node22.next = node23

  # another linked list
  node31 = ListNode(2)
  node32 = ListNode(6)
  node33 = ListNode(7)
  node31.next = node32
  node32.next = node33

  def mergeKLists(lists):
    nodes = []
    head = pointer = ListNode(0)

    for l in lists:
      # l is the head if a linked list, in lists
      while l:
        nodes.append(l.val)
        l = l.next
    nodes.sort()
    for val in nodes:
      pointer.next = ListNode(val)
      pointer = pointer.next

    return head.next


  print(mergeKLists([node11, node21, node31]))
  print(mergeKLists([[]]))




