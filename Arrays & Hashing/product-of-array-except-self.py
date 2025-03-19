from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplication = 1
        flag = []

        for index in range(len(nums)):
            if nums[index] == 0:
                flag.append(index)
                continue
            multiplication *= nums[index]

        if len(flag) > 1:
            return [0] * len(nums)

        for index in range(len(nums)):
            if index in flag:
                nums[index] = multiplication
            elif len(flag):
                nums[index] = 0
            else:
                nums[index] = multiplication // nums[index]

        return nums

solution = Solution()
nums = list(map(int, input().split()))

print(solution.productExceptSelf(nums))