"""
Given the head of a linked list, rotate the list to the right by k places

example 1:

input: head = [1, 2, 3, 4, 5], k = 2
output: [4, 5, 1, 2, 3]

example 2:

input: head = [0, 1, 2], k = 4
output: [2, 0, 1]
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
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    example2 = ListNode(-1)
    example2_node1 = ListNode(0)
    example2_node2 = ListNode(1)
    example2_node3 = ListNode(2)
    example2.next = example2_node1
    example2_node1.next = example2_node2
    example2_node2.next = example2_node3

    print(head.next)
    print(example2.next)

    def rotateRight(head, k):

        # 0 node
        if not head:
            return None

        # 1 node
        if not head.next:
            return head

        # more than 1 node
        n = 0
        ptr = tail = head

        while ptr.next:
            ptr = ptr.next
            n += 1
        n += 1

        # no rotation if n == k
        if n == k % n:
            return head

        # find tell
        tail = ptr
        # print(tail)

        # connect the tail with the head to make the linked list a ring
        tail.next = head

        # new head is: n - k % n
        # new tail is n - k % n - 1
        new_head = new_tail = head
        new_tail_count = n - k % n - 1

        while new_tail_count:
            new_tail = new_tail.next
            new_tail_count -= 1

        # get the new head
        new_head = new_tail.next

        # disconnect the ring
        new_tail.next = None

        print(new_head)
        return new_head

    rotateRight(head.next, 2)
    rotateRight(example2.next, 4)


"""
time: O(N)
- to get the tail of the linked list
space: O(1)
- only use constant amount of pointer

rotation is associate with module

"""
