# https://leetcode.com/problems/richest-customer-wealth/


def maximum_wealth(accounts: list[list[int]]) -> int:
    
    return max(map(sum, accounts))


# Tests
print(maximum_wealth([[2,8,7],[7,1,3],[1,9,5]]))