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
class Node:

  # funtion to init the node object
  def __init__(self, val):
    self.val = val
    self.next = None

# Linked list class contains a Node object
class LinkedList:

  # Function to init head
  def __init__(self):
    self.head = None

  def __str__(self):

    # defining a blank result variable
    result = ""

    # initializing ptr to head
    ptr = self.head

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
if __name__ == '__main__':

  # start with the empty list
  LinkedList = LinkedList()

  # creating nodes
  LinkedList.head = Node(1)
  second = Node(2)
  third = Node(3)

  # connecting nodes
  LinkedList.head.next = second
  second.next = third
  # when print is called, the str method is being called

  def mergeKLists(lists):



  mergeKLists()
