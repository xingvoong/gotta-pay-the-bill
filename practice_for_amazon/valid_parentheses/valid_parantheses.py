"""
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

"""


def isValid(s):
    # use a stack: FILO
    # use a hashmap to match closing and opening
    # when I see a closing bracket.  I need to pop from stack
    # and check whether it is a good match
    # in the end, the stack needs to be empty
    matching_closing = {")": "(", "}": "{", "]": "["}
    if len(s) < 2:
        return False
    stack = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        elif i == ")" or i == "}" or i == "]":
            if len(stack) != 0:
                closing = i
                opening = stack.pop()
                if matching_closing[closing] != opening:
                    return False
            else:
                return False
    return len(stack) == 0
    # return True


def test():
    input = ["()", "()[]{}", "(]", "[", "((", "){"]
    expected = [True, True, False, False, False, False]
    count = 0
    for i in input:
        actual = isValid(i)
        if actual != expected[count]:
            print("Wrong at input: {count}".format(count=count))
            temp = expected[count]
            print("Expected: {temp} but got {actual}".format(temp=temp, actual=actual))
            return
        count += 1

    print("Passed tests")


test()

"""
runtime: O(N)
space: O(N), worse case is all opening brackets.

"""
