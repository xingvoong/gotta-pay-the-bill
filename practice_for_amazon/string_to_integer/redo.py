def myAtoi(s):
    result = 0
    sign = 1
    MAX_INT = pow(2, 31) - 1
    MIN_INT = -pow(2, 31)
    index = 0
    n = len(s)

    # rule 1: remove leading white space
    while index < n and s[index] == " ":
        index += 1

    # rule 2: check for the sign
    if index < n and s[index] == "-":
        sign = -1
        index += 1
    elif index < n and s[index] == "+":
        sign = 1
        index += 1

    # rule 3:
    while index < n and s[index].isdigit():
        # rule 4
        digit = int(s[index])
        # rule 5
        # the bound is too big if I do result > MAX_INT
        # I could make it smaller bound by doing: MAX_INT // 10
        if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > MAX_INT % 10):
            if sign == 1:
                return MAX_INT
            else:
                return MIN_INT

        result = result * 10 + digit
        index += 1

    return sign * result


def test():
    input = ["42", "   -42", "4193 with words", "214748363", "+1"]
    expected = [42, -42, 4193, 214748363, 1]
    count = 0
    for i in input:
        actual = myAtoi(i)
        if actual != expected[count]:
            print("Wrong at input: {count}".format(count=count))
            temp = expected[count]
            print("Expected: {temp} but got {actual}".format(temp=temp, actual=actual))
            return
        count += 1

    print("Passed tests")


test()
