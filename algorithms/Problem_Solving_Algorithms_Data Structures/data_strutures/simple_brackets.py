def checker(symbol_string):
    counter = 0
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced and counter >= 0:
        symbol = symbol_string[index]
        if symbol == "(":
            counter += 1
        else:
            if counter == 0:
                balanced = False
            else:
                counter -= 1

        index += 1

    return bool(balanced and counter == 0)


assert checker('((()))') is True
assert checker('()') is True

assert checker('(') is False
assert checker(')') is False

assert checker('((') is False
assert checker('))') is False

assert checker('(()') is False
assert checker('()()()()()') is True
