# a linked list consists of 2 parts:
# a head and nodes
# so we need 2 classes for this
# a node class and a linked list class,
# for node class, we need val and next
# for linked list class, we need head

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
  print(LinkedList)
