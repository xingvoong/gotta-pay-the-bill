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
      return result


# Code execution
if __name__ == '__main__':
  head = ListNode(0)
  node1 = ListNode(1)
  node2 = ListNode(2)
  head.next = node1
  node1.next = node2
  print(head)