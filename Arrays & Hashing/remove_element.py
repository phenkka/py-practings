from typing import List

class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        str_nums = "".join(map(str, nums)).replace(str(val), "_")
        return len(str_nums) - str_nums.count("_")

    def removeElement2(self, nums: List[int], val: int) -> int:
        count = 0

        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count

solution = Solution()
nums = list(map(int, input().split()))
val = int(input())

print(solution.removeElement1(nums, val))
print()
print(solution.removeElement2(nums, val))