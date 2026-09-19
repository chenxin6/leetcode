from typing import List


class Solution:
    n: int
    m: int
    dp: List[List[int]]

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.dp: List[List[int]] = [[-1 for _ in range(self.m)] for _ in range(self.n)]
        res = self.my_method(matrix, 0, 0)
        for i in range(self.n):
            for j in range(self.m):
                if self.dp[i][j] > res:
                    res = self.dp[i][j]
        return res * res

    def my_method(self, matrix: List[List[str]], index_i: int, index_j: int) -> int:
        if index_i >= self.n or index_j >= self.m:
            return 0
        if self.dp[index_i][index_j] != -1:
            return self.dp[index_i][index_j]
        res = 0
        temp_min = min(
            self.my_method(matrix, index_i + 1, index_j),
            self.my_method(matrix, index_i, index_j + 1),
        )
        for i in range(temp_min + 1):
            if (
                matrix[index_i][index_j] == "1"
                and matrix[index_i + i][index_j + i] == "1"
            ):
                res = 1 + i
        self.dp[index_i][index_j] = res
        return res


class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                temp_res = self.set_value(
                    matrix,
                    dp,
                    i,
                    j,
                )
                if temp_res > res:
                    res = temp_res
        return res * res

    def set_value(
        self, matrix: List[List[str]], dp: List[List[int]], i: int, j: int
    ) -> int:
        res = 1 if matrix[i][j] == "1" else 0
        temp_min = 0
        if res == 1 and i - 1 >= 0 and j - 1 >= 0:
            temp_min = min(dp[i - 1][j], dp[i][j - 1])
            if matrix[i - temp_min][j - temp_min] == "1":
                res = temp_min + 1
            else:
                res = temp_min
        dp[i][j] = res
        return res


input_matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
input_matrix = [
    ["1", "0", "1", "1", "1", "0", "0", "0", "1", "0"],
    ["0", "1", "0", "0", "0", "0", "0", "1", "1", "0"],
    ["0", "1", "0", "1", "0", "0", "0", "0", "1", "1"],
    ["1", "1", "1", "0", "0", "0", "0", "0", "1", "0"],
    ["0", "1", "1", "1", "0", "0", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "1", "0", "1", "1", "1", "0"],
]
input_matrix = [
    ["0", "0", "1", "0"],
    ["1", "1", "1", "1"],
    ["1", "1", "1", "1"],
    ["1", "1", "1", "0"],
    ["1", "1", "0", "0"],
    ["1", "1", "1", "1"],
    ["1", "1", "1", "0"],
]
print(Solution().maximalSquare(input_matrix))
