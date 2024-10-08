from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        self.merge_sort(citations, 0, len(citations) - 1)
        res = 0
        for n in range(1, len(citations) + 1):
            index = len(citations) - n
            value = citations[index]
            if value >= n:
                res = n
        return res
    def merge_sort(self, citations: List[int], left: int, right: int):
        if left >= right:
            return citations
        mid = (left + right) // 2
        self.merge_sort(citations, left, mid)
        self.merge_sort(citations, mid + 1, right)
        self.merge(citations, left, mid, right)
    def merge(self, citations: List[int], left: int, mid: int, right: int):
        i = left
        j = mid + 1
        temp_res = []
        while i <= mid and j <= right:
            if citations[i] <= citations[j]:
                temp_res.append(citations[i])
                i += 1
            else:
                temp_res.append(citations[j])
                j += 1
        while i <= mid:
            temp_res.append(citations[i])
            i += 1
        while j <= right:
            temp_res.append(citations[j])
            j += 1
        citations[left: right + 1] = temp_res


s = Solution()
res = s.hIndex([3,0,6,1,5])
print(res)
