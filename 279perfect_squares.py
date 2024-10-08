from typing import List

class Solution:
    def numSquares(self, n: int) -> int:
        dp_arr = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            j = 1
            while i - j * j >= 0:
                dp_arr[i] = min(dp_arr[i], 1 + dp_arr[i - j * j])
                j += 1
        return dp_arr[n]
    def numSquares2(self, n: int) -> int:
        dp_arr = [-1 for i in range(n + 1)]
        dp_arr[0] = 0
        return self.dp(n, dp_arr)
    def dp(self, n: int, dp_arr: List[int]) -> int:
        if dp_arr[n] != -1:
            return dp_arr[n]
        res = n
        j = 1
        while n - j * j >= 0:
            res = min(res, 1 + self.dp(n - j * j, dp_arr))
            j += 1
        dp_arr[n] = res
        return res


s = Solution()
res = s.numSquares(285)
print(res)
