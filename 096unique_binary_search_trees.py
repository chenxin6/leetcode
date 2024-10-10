def get_unique_binary_search_trees_num(n):
    if n == 0 or n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    res = 0
    for i in range(n):
        res += get_unique_binary_search_trees_num(i) * get_unique_binary_search_trees_num(n - 1 - i)
    dp[n] = res
    return res


class Solution:
    dp = []

    def numTrees(self, n: int) -> int:
        self.dp = [-1 for _ in range(n + 1)]
        self.dp[0] = 1
        self.dp[1] = 1
        self.my_method(n)
        return self.dp[n]

    def my_method(self, n):
        if self.dp[n] != -1:
            return self.dp[n]
        res = 0
        for i in range(1, n + 1):
            res += self.my_method(i - 1) * self.my_method(n - i)
        self.dp[n] = res
        return res


n = 2
dp = [-1 for _ in range(n + 1)]
print(get_unique_binary_search_trees_num(n))
