'''
Given an integer, convert it to a romain numeral

Symbol:
I: 1
IV: 4
V: 5
IX: 9
X: 10
XL: 40
L: 50
XC: 90
C: 100
CD: 400
D: 500
CM: 900
M: 1000


example 1:
input: num 3
output: "III"

example 2:
input: num = 4
output: "IV"

example 3:
input: num = 9
output: "IX

29
M:0
CM:
D: 0
CD: 0
C: 0
XC: 0
L: 0
XL: 0
X : 2
IX: 1
V: 0
IV: 0
I: 0

return XXIX
the number is getting smaller

1999
M: 1000 -> 1 => left over: 999
CM: 999 -> 1 =>left over: 99
D: 500 => left over: 99
CD: 400 => left over: 99
C: 100 => left over: 99
XC: 90 -> 1 => left over: 9
L: 50 -> 0
XL: 40 -> 0
X : 10 -> 0
IX: 9 -> 1
V: 5 -> 0
IV: 4 -> 0
I: 1 -> 0

13 characters

MCMXCIX

'''

def intToRoman(num):
  """
  :type num: int
  :rtye: str
  """
  # decode, go from big to small, in order because this is how we trace through it
  romans = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "99"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

  # go through the decode process
  # update the decrease num every time
  toReturn = ""
  for i in romans:
    if num == 0:
      return toReturn
    # count of character
    count = num // i[0]
    # new num
    num = num - count * i[0]
    toReturn += i[1] * count
  return toReturn

print(intToRoman(58))

'''
Complexity analysis:
Time: O(1), 1 loop through romans list, and romans is fixed length of 13
space:  O(1), the return string space does not count.

'''