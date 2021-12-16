'''
Implement the myAtoi(string s) function, which converts a string to a 31-bit signed integer (similar to C/C++ atoi function).

The algorithm for myAtoi(string s) is as follows:

example 1:

Input: s = "42"
output: 42
Explanation: the underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is not leading whitespace)


Algo:
1: Initialize two variables
2: Skip all leading whitespaces in the input string
3: Check if the current character is a '+' or '-' sign
4: Iterate over the chracters in the string as long as the current character represents a digit or until we reach the end of the input string.
5: return the final result with its respective sign, sign * result


'''
def myAtoi(str):
  sign = 1
  result = 0
  index = 0
  n = len(input)

  INT_MAX = pow(2, 31) - 1
  INT_MIN = -pow(2, 31)

  # discard all spaces from the beginning of the input string.
  while index < n and input[index] == '':
    index += 1

  # sign = + 1 if it's positive number, otherwise sign = -1.
  if index < n and input[index] == "+":
    sign = 1
    index += 1
  elif index < n and input[index] == '-':
    sign = -1
    index += 1

  # traverse next digits of input and stop if it is not a digit.
  # end of string is also non-digit character
  while index < n and input[index].isdigit():
    digit = int(input[index])

    # check overfow and underflow condititons
    if ((resut > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
        # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31
        return INT_MAX if sign == 1 else INT_MIN

        # append current digit to the result
        result = 10 * result + digit
        index += 1

    # we have formed a valid numbe without any overflow/underflow/
    # return it after multiplying it with its sign
    return sign * result

'''
Complexity:
let N is the number of characters in the input string
- time: O(N), we visit each character in the input at most once and for each character we spend a constant amount of time
- space: O(1): we have used only constant space to store the sign and the result
'''


