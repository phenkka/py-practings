from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_v = 0

        while left < right:
            print(left, right)
            print(min(height[left], height[right]) * (right - left))
            max_v = max(max_v, min(height[left], height[right]) * (right - left))
            print(max_v)
            print()

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_v

solution = Solution()
height = list(map(int, input().split()))

print(solution.maxArea(height))