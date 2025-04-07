from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        first_heap, second_heap = sum(nums), 0

        for index in range(len(nums)):
            first_heap -= nums[index]
            if first_heap == second_heap:
                return index
            second_heap += nums[index]

        return -1

solution = Solution()
nums = list(map(int, input().split()))

print(solution.pivotIndex(nums))