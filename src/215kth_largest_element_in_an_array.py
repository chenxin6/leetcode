from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp_arr = [-1000000 for _ in range(k)]
        for num in nums:
            self.insert_arr(temp_arr, num, 0, k - 1)
        return temp_arr[0]

    def insert_arr(self, arr: List[int], value: int, start: int, end: int) -> None:
        if value >= arr[end]:
            arr.insert(end + 1, value)
            arr.pop(0)
            return
        if start >= end or value <= arr[start]:
            arr.insert(start, value)
            arr.pop(0)
            return
        mid = (start + end) // 2
        if arr[mid] < value:
            self.insert_arr(arr, value, mid + 1, end)
        elif arr[mid] > value:
            self.insert_arr(arr, value, start, mid - 1)
        else:
            arr.insert(mid, value)
            arr.pop(0)


def main():
    arr = [3, 2, 1]
    s = Solution()
    res = s.findKthLargest(arr, 3)
    print(res)


if __name__ == "__main__":
    main()
