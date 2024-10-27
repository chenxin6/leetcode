from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = [mat[0][0]]
        n = len(mat)
        m = len(mat[0])
        if n == 1 and m == 1:
            return res
        last_i = 0
        last_j = 0
        go_down = False
        go_up = True
        for i in range(2, n * m + 1):
            # print(mat[last_i][last_j])
            if go_down:
                if last_i + 1 == n:
                    res.append(mat[last_i][last_j + 1])
                    last_j = last_j + 1
                    go_down = False
                    go_up = True
                elif last_j == 0:
                    res.append(mat[last_i + 1][last_j])
                    last_i = last_i + 1
                    go_down = False
                    go_up = True
                else:
                    res.append(mat[last_i + 1][last_j - 1])
                    last_i = last_i + 1
                    last_j = last_j - 1
                continue
            if go_up:
                if last_j == m - 1:
                    res.append(mat[last_i + 1][last_j])
                    last_i = last_i + 1
                    go_down = True
                    go_up = False
                elif last_i == 0:
                    res.append(mat[last_i][last_j + 1])
                    last_j = last_j + 1
                    go_down = True
                    go_up = False
                else:
                    res.append(mat[last_i - 1][last_j + 1])
                    last_i = last_i - 1
                    last_j = last_j + 1
                continue
        return res


s = Solution()
print(s.findDiagonalOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
))
