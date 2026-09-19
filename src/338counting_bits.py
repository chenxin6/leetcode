class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        for i in range(n + 1):
            count = 0
            while i != 0:
                if i % 2 == 1:
                    count += 1
                i = i // 2
            res.append(count)
        return res


print(Solution().countBits(5))
