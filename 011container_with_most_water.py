def get_water_area(arr):
    start = 0
    end = len(arr) - 1
    res = 0
    while start < end:
        temp = (end - start) * get_min(arr[start], arr[end])
        if temp > res:
            res = temp
        if arr[start] < arr[end]:
            start = start + 1
        else:
            end = end - 1
    return res


def get_water_area2(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            temp = (j - i) * get_min(arr[i], arr[j])
            if temp > res:
                res = temp
    return res


def get_min(i, j):
    if i >= j:
        return j
    else:
        return i


arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(get_water_area(arr))
