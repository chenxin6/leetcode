from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        while left < right:
            if left + 1 == right:
                left = right if self.is_ok(citations, right) else left
                break
            mid = (left + right) // 2
            if self.is_ok(citations, mid):
                left = mid
            else:
                right = mid
        return left
    def is_ok(self, citations: List[int], n: int) -> bool:
        if n < 0 or n > len(citations):
            return False
        if n == 0:
            return True
        index = len(citations) - n
        value = citations[index]
        return value >= n


s = Solution()
res = s.hIndex([0,1,3,5,6])
print(res)
