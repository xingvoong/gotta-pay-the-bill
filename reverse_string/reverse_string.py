'''
write a function that reverses a string.
The input string is given as an array of
characters s

You must do this by modifying the input array
in place with O(1) extra memory

'''

def reverseString(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]
print(reverseString(s1))
print(reverseString(s2))

'''
runtime: O(N)
space: O(1)

'''

