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
    
n = 2
dp = [-1 for _ in range(n + 1)]
print(get_unique_binary_search_trees_num(n))