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
  nodeA = ListNode(-101)
  nodeA1 = ListNode(1)
  nodeA2 = ListNode(4)
  nodeA3 = ListNode(5)
  nodeA.next = nodeA1
  nodeA1.next = nodeA2
  nodeA2.next = nodeA3

  # another linked list
  nodeB = ListNode(-101)
  nodeB1 = ListNode(1)
  nodeB2 = ListNode(3)
  nodeB3 = ListNode(4)
  nodeB.next = nodeB1
  nodeB1.next = nodeB2
  nodeB2.next = nodeB3

  # another linked list
  nodeC = ListNode(-101)
  nodeC1 = ListNode(2)
  nodeC2 = ListNode(6)
  nodeC3 = ListNode(7)
  nodeC.next = nodeC1
  nodeC1.next = nodeC2
  nodeC2.next = nodeC3

  def mergeTwoLists(l1, l2):
    toReturn = ptr = ListNode(-101)
    while l1 and l2:
      if l1.val <= l2.val:
        ptr.next = l1
        l1 = l1.next
      else:
        ptr.next = l2
        l2 = l2.next
      ptr = ptr.next

    if not l1:
      ptr.next = l2
    else:
      ptr.next = l1

    return toReturn.next

  def mergeKLists(lists):
    # [list1, list2, list3]
    n = len(lists)
    if n < 1:
      return []
    count = 0
    newList = lists[0]
    # newList = mergeTwoLists(lists[0], lists[1])
    # return mergeTwoLists(newList, lists[2])
    # return newList
    while count < n-1:
      newList = mergeTwoLists(newList, lists[count+1])
      count += 1

    return newList




  print(mergeKLists([nodeA.next, nodeB.next, nodeC.next]))
  print(mergeKLists([[]]))
  print(mergeKLists([]))
  # print(mergeTwoLists(nodeA.next, nodeB.next))


  '''
  let N be the total number of node
  let K be the number of linked list in lists
  time: O(kN)
  space: O(1), the return result space does not count toward the complexity

  '''




