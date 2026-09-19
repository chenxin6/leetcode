class Solution:
    has_flag_dp: list[int]
    no_flag_dp: list[int]

    def maxProfit(self, prices: list[int]) -> int:
        self.has_flag_dp = [-1 for _ in range(len(prices))]
        self.no_flag_dp = [-1 for _ in range(len(prices))]
        return self.my_method(prices, 0, False)

    def my_method(self, prices: list[int], index: int, has_flag: bool) -> int:
        if index >= len(prices):
            return 0
        if index == len(prices) - 1 and has_flag:
            return prices[index]
        if has_flag and self.has_flag_dp[index] != -1:
            return self.has_flag_dp[index]
        if not has_flag and self.no_flag_dp[index] != -1:
            return self.no_flag_dp[index]
        res = 0
        temp_res = 0
        if has_flag:
            temp_res = max(
                self.my_method(prices, index + 1, True),
                prices[index] + self.my_method(prices, index + 2, False),
            )
        else:
            temp_res = max(
                self.my_method(prices, index + 1, False),
                self.my_method(prices, index + 1, True) - prices[index],
            )
        if temp_res > res:
            res = temp_res
        if has_flag:
            self.has_flag_dp[index] = res
        else:
            self.no_flag_dp[index] = res
        return res


print(Solution().maxProfit([1, 2, 3, 0, 2]))
