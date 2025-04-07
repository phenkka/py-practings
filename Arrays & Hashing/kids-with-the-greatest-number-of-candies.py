from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result

solution = Solution()
candies = list(map(int, input().split()))
extra_candies = int(input())

print(solution.kidsWithCandies(candies, extra_candies))