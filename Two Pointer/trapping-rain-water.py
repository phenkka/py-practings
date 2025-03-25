from typing import List

class Solution():
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]

        return result

solution = Solution()
height = list(map(int, input().split()))

print(solution.trap(height))