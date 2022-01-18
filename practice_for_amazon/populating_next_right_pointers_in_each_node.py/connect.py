'''
you are given a perfect binary tree where all leaves are on the same level, and every parent has 2 children.  The binary tree has the following definition:

struct Node {
  int val
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node.  If there is no next right node, the next pointer should be set to NULL

Initially, all next pointers are set to NULL

example 1:
root = [1, 2, 3, 4, 5, 6, 7]
output = [1, #, 2, 3, #, 4, 5, 6, 7, #]

example 2:
root = []
output = []

Constraint:
the number of nodes in the trees is in the range(0, 2^12 - 1)
-1000 <= Node.val <= 1000
'''