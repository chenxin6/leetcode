from typing import List


class Solution:

    def my_method(self, nums: List[int], index: int, can_rob: bool, db: dict) -> int:
        if index >= len(nums):
            return 0
        key = str(index) + "-" + str(can_rob)
        if db.get(key) is not None:
            return db[key]
        res = 0
        if can_rob:
            res = nums[index] + self.my_method(nums, index + 1, False, db)
        temp_res = self.my_method(nums, index + 1, True, db)
        res = max(res, temp_res)
        db[key] = res
        return res

    def rob(self, nums: List[int]) -> int:
        db = {}
        db2 = {}
        res = nums[0] + self.my_method(nums[0 : len(nums) - 1], 1, False, db)
        temp_res = self.my_method(nums, 1, True, db2)
        return max(res, temp_res)


s = Solution()
print(s.rob([2, 3, 2]))
