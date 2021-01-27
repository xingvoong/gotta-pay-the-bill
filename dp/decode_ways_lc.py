'''
1. mediyum , dp

2. message containing letters from A-Z can be
encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message,
all the digits must be mapped back into letters
using the reverse of the mapping above
(there may be multiple ways).
For example, "111" can have each of its "1"s be mapped into 'A's to make "AAA",
or it could be mapped to "11" and "1" ('K' and 'A' respectively) to make "KA".
Note that "06" cannot be mapped into 'F' since "6" is different from "06".

Given a non-empty string num containing only digits,
return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.


Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26),
"VF" (22 6), or "BBF" (2 2 6).

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20".
Since there is no character,
there are no valid ways to decode this since all digits need to be mapped.

3: Solution in plain English or pseudocode
Intuition:
at a given index, it can be a single digit decode or a double digit decode

2 approach:

I: dp with table.
initialize dp table, table[0] = 1
+ if the string starts with 0:
    table[1] = 0
+ else:
    table[1] = 1
to fill the table with the result
+ iterate start from index 2:
    + single digit decode:
        + if the current character is not 0:
            table[index] = table[index-1]

    + double digit decode:
        + if the current and the previous character are
            bigger than 10 and less then 26:
            table[index] += table[index-2]
return last element of table, table[-1]


II: dp with 2 pointers.
an improvement with space from dp with table
instead of using the whole table,
we only 2 variable back_one, back_two
to store the decoding results

4: implementation

'''


def num_coding_table(s):
    """
        :type s: str
        :rtype: int
    """
    table = [0 for _ in range(len(s) + 1)]
    table[0] = 1

    if s[0] == "0":
        table[1] = 0
    else:
        table[1] = 1

    for i in range(2, len(table)):
        if s[i - 1] != 0:
            table[i] = table[i-1]
        two_digit = int(s[i-2:i])
        if two_digit >= 10 and two_digit <= 26:
            table[i] += table[i-2]

    return table[-1]


def num_coding_pointer(s):
    if s[0] == '0':
        return 0
    back_one = 1
    back_two = 1
    for i in range(1, len(s)):
        current = 0
        if s[i] != 0:
            current = back_one
        two_digit = int(s[i-1:i+1])
        if two_digit >= 10 and two_digit <= 26:
            current += back_two
        back_two = back_one
        back_one = current

    return back_one


assert num_coding_table("12") == 2
assert num_coding_table("226") == 3
assert num_coding_table("0") == 0
assert num_coding_table("1") == 1
assert num_coding_table("11111111111111111") == 2584

assert num_coding_pointer("12") == 2
assert num_coding_pointer("226") == 3
assert num_coding_pointer("0") == 0
assert num_coding_pointer("1") == 1
assert num_coding_pointer("11111111111111111") == 2584


'''
5: complexity analysis.
let N be the length of string s.

approach 1, num_coding_table(s)
time: O(N), iterate through s
space: O(N), for the table

approach 2, num_coding_pointer(s)
time: O(N), iterate through s
space: O(1), only for 2 variable
'''
