class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.my_method(num)
        return num
    def my_method(self, num: int) -> int:
        res = 0
        while num > 0:
            res += num % 10
            num = num // 10
        return res


s = Solution()
res = s.addDigits(44)
print(res)
