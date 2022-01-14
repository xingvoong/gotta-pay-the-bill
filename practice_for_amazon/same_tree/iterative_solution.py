'''
Given the roots of 2 binary trees p and q, write a function to check if they are the same or not. Solve this recursively

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value

Example:
input:
p = [1, 2, 3]
q = [1, 2, 3]

Output: true

input: p = [1, 2], q = [1, null, 2]
output: false

input: p = [1, 2, 1], q = [1, 1, 2]
output: false

- the number of nodes in both trees is in the range [0, 100]
- -10^4 <= Node.val <= 10^4
'''