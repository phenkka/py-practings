from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for left in range(len(nums)):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid, right = left + 1, len(nums) - 1

            while mid < right:
                sum_three = nums[left] + nums[mid] + nums[right]

                if sum_three < 0:
                    mid += 1
                elif sum_three > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1

                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result

solution = Solution()
nums = list(map(int, input().split()))

print(solution.threeSum(nums))