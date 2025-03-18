from typing import List

class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        mhash = {}

        for num in nums:
            mhash[num] = mhash.get(num, 0) + 1

        for key, value in mhash.items():
            if value > 1:
                return True
        return False

solution = Solution()

nums = list(map(int, input().split()))

print(f"First solution - {solution.containsDuplicate1(nums)}")
print()
print(f"Second solution - {solution.containsDuplicate2(nums)}")