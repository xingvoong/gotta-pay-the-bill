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