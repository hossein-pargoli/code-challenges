# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/


def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:

    # soldier_numbers = { k:v for k, v in enumerate(map(sum, mat)) }
    # sorted_soldier_numbers = dict(sorted(soldier_numbers.items(), key=lambda item: item[1]))
    # result = [ i for i in sorted_soldier_numbers.keys() ]
    # return result[:k]

    rows = sorted( range(len(mat)), key=lambda i: mat[i] )
    return rows[:k]


# Tests
matrix = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
print(k_weakest_rows(matrix, 3))