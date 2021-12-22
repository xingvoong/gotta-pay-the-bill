'''
Given a string s containing just the characters '(', ')', '{', '}', '[', ']', determine if the input string is valid

an input string is valid if:
1: Open brackets must be closed by the same type of brackets
2: Open brackets must be closed in the correct order

Example:
I: s = "()"
O: true

Example:
Input: s = "()[]{}"
output: true

Example 3:
Input: s = "(]"
O: False

'''
def isValid(s):
