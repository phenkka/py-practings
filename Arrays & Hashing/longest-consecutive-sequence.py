from typing import List

class QuickSort:
    @staticmethod
    def sort(nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        pivot = len(nums) // 2

        left = [num for num in nums if num < pivot]
        mid = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]

        return QuickSort.sort(left) + mid + QuickSort.sort(right)

class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        count, current_count = 1, 1

        if not nums:
            return 0

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i + 1] - sorted_nums[i] == 1:
                current_count += 1
            else:
                count = max(current_count, count)
                current_count = 1

        return max(count, current_count)

    def longestConsecutive2(self, nums: List[int]) -> int:
        nums = QuickSort.sort(list(set(nums)))
        count, current = 1, 1

        for index in range(len(nums) - 1):
            if nums[index+1] - nums[index] == 1:
                current += 1
            else:
                count = max(count, current)
                current = 1

        return max(count, current)

solution = Solution()
nums = list(map(int, input().split()))

print(f"First solution - {solution.longestConsecutive1(nums)}")
print()
print(f"Second solution - {solution.longestConsecutive2(nums)}")