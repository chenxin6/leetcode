def get_min_jump(arr, index, last_max_reach):
    if index == len(arr) - 1:
        return 0
    if arr[index] + index >= len(arr) - 1:
        return 1
    if arr[index] == 0:
        return 10001
    if dp[index] != -1:
        return dp[index]
    res = 10001
    max_reach = index + arr[index]
    for i in range(last_max_reach + 1 - index, arr[index] + 1):
        temp = 1 + get_min_jump(arr, index + i, max_reach)
        if temp < res:
            res = temp
    dp[index] = res
    return res


arr = [2, 3, 1, 1, 4]
dp = [-1 for _ in range(len(arr))]
print(get_min_jump(arr, 0, 0))
