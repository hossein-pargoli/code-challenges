# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/


def number_of_steps(num: int) -> int:
    
    steps = 0
    
    while num != 0:

        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        
        steps += 1
    
    return steps


def number_of_steps_bitwise(num: int) -> int:
    
    steps = 0
    
    while num != 0:

        if num & 1 == 0:
            num >>= 1
        else:
            num -= 1
        
        steps += 1
    
    return steps


# Tests
print(number_of_steps_bitwise(14))
print(number_of_steps_bitwise(8))
print(number_of_steps_bitwise(123))