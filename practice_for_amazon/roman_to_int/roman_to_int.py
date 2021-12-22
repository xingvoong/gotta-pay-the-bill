"""
Roman numerals are presented by seven different symbols: I, V, X, L, C D and M.

if I go forward I would never know which character I need
but if I go backward I would because it is a subtract character
Hint: working the string from back to front and using a map

# the trick here is to go backward:
        # if the current number is less than the previous number:
        # than subtract the current number
        # otherwise, add the current number
        # it is easier to think in term of current number when we do
        # a foor lop or while loop with i
"""


def romanToInt(s):
    decode = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = len(s)
    result = decode[s[n - 1]]
    previous = result

    for i in range(n - 2, -1, -1):
        current = decode[s[i]]
        if current < previous:
            result -= current
        else:
            result += current
        previous = current

    return result


def test():
    input = ["MCMXCIV", "III", "LVIII", "MCMXCIX"]
    expected = [1994, 3, 58, 1999]
    count = 0
    for i in input:
        actual = romanToInt(i)
        if actual != expected[count]:
            print("Wrong at input: {count}".format(count=count))
            temp = expected[count]
            print("Expected: {temp} but got {actual}".format(temp=temp, actual=actual))
            return
        count += 1

    print("Passed tests")


test()

"""
Complexity:
let N be the length of the string.
time: O(N), go through the string once
space: O(1), constant space for hashmap

"""
