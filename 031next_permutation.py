from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 2 1
        # 1 3 2
        index = len(nums) - 1
        while index >= 0:
            if index == 0 or nums[index] > nums[index - 1]:
                index -= 1
                break
            else:
                index -= 1
        if index != -1:
            for i in range(len(nums) - 1, index, -1):
                if nums[i] > nums[index]:
                    self.swap(nums, i, index)
                    break
        self.reverse_arr(nums, index + 1, len(nums) - 1)

    def reverse_arr(self, nums: List[int], start: int, end: int) -> None:
        index = start
        mid = (start + end) // 2
        while index <= mid:
            self.swap(nums, index, end - (index - start))
            index += 1

    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


def main():
    arr = [3, 2, 1]
    s = Solution()
    s.nextPermutation(arr)
    print(arr)


if __name__ == "__main__":
    main()
