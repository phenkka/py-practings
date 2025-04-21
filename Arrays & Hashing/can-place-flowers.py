from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for index in range(len(flowerbed)):
            if flowerbed[index] == 0 and (index == 0 or flowerbed[index - 1] == 0) and (
                    index == len(flowerbed) - 1 or flowerbed[index + 1] == 0):
                flowerbed[index] = 1
                n -= 1
                if n == 0:
                    return True
        return False

solution = Solution()
flowerbed = list(map(int, input().split()))
n = int(input())

print(solution.canPlaceFlowers(flowerbed, n))