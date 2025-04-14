from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] <= nums[right]:
                left += 1
            elif nums[left] > nums[right]:
                right -= 1
        return right

solution = Solution()
nums = list(map(int, input().split()))

print(solution.findPeakElement(nums))