def quick_sort(arr, left, right):
    if left < 0 or right >= len(arr):
        print("error")
        return
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)
def partition(arr, left, right):
    index = (left + right) // 2
    pivot = arr[index]
    arr[index] = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right = right - 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left = left + 1
        arr[right] = arr[left]
    arr[left] = pivot
    return left

def merge_sort(arr, left, right):
    if left < 0 or right >= len(arr) or left >= right:
        return
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)
def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1
    arr[left: right + 1] = temp

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2, n):
        heap_adjust(arr, n - 1 - i, n)
    for i in range(n):
        swap(arr, 0, n - 1 - i)
        heap_adjust(arr, 0, n - 1 - i)
def heap_adjust(arr, i, n):
    father_value = arr[i]
    while left_child(i) < n:
        child_index = left_child(i)
        if child_index + 1 < n and arr[child_index] < arr[child_index + 1]:
            child_index += 1
        if father_value >= arr[child_index]:
            break
        else:
            arr[i] = arr[child_index]
        i = child_index
    arr[i] = father_value
def left_child(i):
    return 2 * i + 1
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bucket_sort(arr):
    temp = [0 for _ in range(100001)]
    for value in arr:
        index = value + 50000;
        temp[index] = temp[index] + 1
    res = []
    for i in range(100001):
        res = res + [i - 50000 for _ in range(temp[i])]
    return res

def insert_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
def select_sort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = [10, 7, 8, 9, 1, 5, 7, 7, 7] 
n = len(arr) 
# quick_sort(arr, 0, n - 1)
# merge_sort(arr, 0, n - 1)
heap_sort(arr)
# arr = bucket_sort(arr)
# insert_sort(arr)
# select_sort(arr)
# bubble_sort(arr)
print ("Sorted Array:") 
for i in range(n): 
    print ("%d" %arr[i])
