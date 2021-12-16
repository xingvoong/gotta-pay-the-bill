'''
Given a string s, retrun the longest palindromic substring in s

Example 1:
I: "babad"
O: "bab"
Note: "aba" is also a valid answer

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
i: s = "a"
o: "a"

Example 4:
i: s = "ac"
o: "a"

Solution:
- expand from the center:
- the substring is odd length,
- the substring is even length

'''
# a palindrome has the same character if being expanding around center
# there are 2 possible center, depend on odd of even
# a or aa
# 1 center starts at the same character
# another center starts at 2 characters next to each others
def longestPalindrome(s):
  start = 0
  max_len = 0

  def expandAroundCenter(left, right, s):
    nonlocal start
    nonlocal max_len
    while left > -1 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    # the correct bound for palindrome is:
    # l + 1
    # r - 1
    # the length = r - l + 1 = r - 1 - (l + 1) + 1
    # = r - 1 - l - 1 + 1 = r - l - 1
    if right - left - 1 > max_len:
      max_len = right - left - 1
      start = left + 1

  for i in range(len(s)):
    expandAroundCenter(i, i, s)
    expandAroundCenter(i, i+1, s)

  return s[start:start+max_len]

print(longestPalindrome("babad"))

'''
Complexity Analysis:
Time:
- for loop takes O(N) times
- expandAroundCenter takes O(N) times
=> O(N^2) time

Space: O(1) space

'''
