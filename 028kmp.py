def kmp(str1, str2):
    if len(str1) == 0:
        return True
    if len(str1) > len(str2):
        return False
    res = False
    next_arr = get_next_arr(str1)
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        while i > 0 and str1[i] != str2[j]:
            i = next_arr[i - 1]
        if str1[i] == str2[j]:
            i += 1
        if i == len(str1):
            res = True
            break
        j += 1
    return res


def get_next_arr(str1):
    res = [0 for _ in range(len(str1))]
    i = 0
    j = 1
    while i < len(str1) and j < len(str1):
        while i > 0 and str1[i] != str1[j]:
            i = res[i - 1]
        if str1[i] == str1[j]:
            i += 1
        res[j] = i
        j += 1
    return res


str1 = "4747479"
str2 = "47474747474743747474734747s47479272373474747"
print(kmp(str1, str2))
