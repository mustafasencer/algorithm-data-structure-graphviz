"""
    Created by Mustafa Sencer Özcan on 22.05.2020.
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col_0 = False
        is_row_0 = False

        for i in range(len(matrix)):
            if matrix[i][0] is 0:
                is_col_0 = True
                break
        for j in range(len(matrix[0])):
            if matrix[0][j] is 0:
                is_row_0 = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] is 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] is 0 or matrix[0][j] is 0:
                    matrix[i][j] = 0

        if is_col_0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if is_row_0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        return matrix


if __name__ == '__main__':
    result = Solution().setZeroes([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    print(result)
