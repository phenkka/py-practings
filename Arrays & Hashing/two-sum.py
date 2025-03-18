from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for key, value in enumerate(nums):
            needed = target - value

            if needed in seen:
                return [key, seen[needed]]

            seen[value] = key

solution = Solution()
nums = list(map(int, input().split()))
target = int(input())

print(solution.twoSum(nums, target))