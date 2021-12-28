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
            return []


# Code execution
if __name__ == "__main__":

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
                # move the head, slicing change the head
                l1 = l1.next
            else:
                ptr.next = l2
                # move the head, slicing change the head
                l2 = l2.next
            # remember to move this pointer as well
            ptr = ptr.next

        if not l1:
            ptr.next = l2
        else:
            ptr.next = l1

        return toReturn.next

    def mergeKLists(lists):

        n = len(lists)
        if n < 1:
            return
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    # print(mergeTwoLists(nodeA.next, nodeB.next))
    print(mergeKLists([nodeA.next, nodeB.next, nodeC.next]))

"""
Complexity:
time: O(NlogK), interval increase double each time, that is logK to mergeK list
we call it N time for number of node

space: O(1), use constant space

"""
