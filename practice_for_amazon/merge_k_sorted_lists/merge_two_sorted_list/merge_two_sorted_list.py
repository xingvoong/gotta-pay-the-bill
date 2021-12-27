"""
You are given the heads of 2 sorted linked lists list1 and list2.
Merge two lists in a one sorted list.  The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list
"""

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
    # create linked list A
    headA = ListNode(-101)

    nodeA1 = ListNode(1)
    nodeA2 = ListNode(2)
    nodeA3 = ListNode(4)
    nodeA4 = ListNode(5)

    headA.next = nodeA1
    nodeA1.next = nodeA2
    nodeA2.next = nodeA3
    nodeA3.next = nodeA4

    # create linked list B
    headB = ListNode(-101)

    nodeB1 = ListNode(1)
    nodeB2 = ListNode(3)
    nodeB3 = ListNode(4)

    headB.next = nodeB1
    nodeB1.next = nodeB2
    nodeB2.next = nodeB3

    def mergedTwoLists(l1, l2):
        mergedList = ptr = ListNode(-101)
        # the list is made by slicing together the nodes of the first 2 lists
        # if list1[0] < list2[0]:
        # list1[0] + mergeTwoList(list1[1:], list2)
        # else:
        # list2[0] + mergeTwoList(list1, list2[1:])
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                # slicing, list1[1:]
                l1 = l1.next
            else:
                ptr.next = l2
                # slicing, list2[2:]
                l2 = l2.next
            ptr = ptr.next

        if l1 is not None:
            ptr.next = l1
        else:
            ptr.next = l2

        return mergedList.next

        return mergedList.next

    print("linked list A ", headA.next)
    print("linked list B ", headB.next)
    print(mergedTwoLists(headA.next, headB.next))

"""
let M be the number of nodes in list 1
let N be the number of nodes in list 2
time: O(M + N)
space: O(1), only allocate pointers
"""
