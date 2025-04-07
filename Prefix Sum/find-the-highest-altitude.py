from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        peek = 0
        current_point = 0

        for point in gain:
            current_point += point
            peek = max(peek, current_point)

        return peek

solution = Solution()
gain = list(map(int, input().split()))

print(solution.largestAltitude(gain))