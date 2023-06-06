# https://leetcode.com/problems/roman-to-integer/


def roman_to_integer(string: str) -> int:

    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    decimal = 0

    for i in range(len(string) - 1):
        if roman[string[i]] < roman[string[i + 1]]:
            decimal -= roman[string[i]]
        else:
            decimal += roman[string[i]]

    return decimal + roman[string[-1]]


# Tests
print(f'III = {roman_to_integer("III")}')
print(f'IX = {roman_to_integer("IX")}')
print(f'LVIII = {roman_to_integer("LVIII")}')
print(f'MCMXCIV = {roman_to_integer("MCMXCIV")}')


# 4     IV
# 9     IX
# 40    XL
# 90    XC
# 400   CD
# 900   CM