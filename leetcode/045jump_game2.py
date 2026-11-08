from typing import List


class Solution:
    dp: list[int]

    def jump(self, nums: List[int]) -> int:
        self.dp = [-1 for _ in range(len(nums))]
        return self.my_method(nums, 0)

    def my_method(self, nums: List[int], index: int) -> int:
        if index >= len(nums) - 1:
            return 0
        if self.dp[index] != -1:
            return self.dp[index]
        res = 999999999
        for i in range(1, nums[index] + 1):
            res = min(res, 1 + self.my_method(nums, index + i))
        self.dp[index] = res
        return res


print(Solution().jump([2, 3, 1, 1, 4]))
