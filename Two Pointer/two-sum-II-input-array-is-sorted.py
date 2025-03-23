from typing import List

class Solution:
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        mhash = {}

        for key, value in enumerate(numbers):
            needed = target - value

            if needed in mhash:
                return sorted([key + 1, mhash[needed] + 1])

            mhash[value] = key

solution = Solution()
numbers = list(map(int, input().split()))
target = int(input())

print(f"First solution - {solution.twoSum1(numbers, target)}")
print()
print(f"Second solution - {solution.twoSum2(numbers, target)}")