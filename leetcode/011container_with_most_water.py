from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr = height
        start = 0
        end = len(arr) - 1
        res = 0
        while start < end:
            temp = (end - start) * min(arr[start], arr[end])
            if temp > res:
                res = temp
            if arr[start] < arr[end]:
                start = start + 1
            else:
                end = end - 1
        return res

    def maxArea2(self, height: List[int]) -> int:
        arr = height
        res = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                temp = (j - i) * min(arr[i], arr[j])
                if temp > res:
                    res = temp
        return res


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
