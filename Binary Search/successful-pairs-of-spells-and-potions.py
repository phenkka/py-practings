from typing import List
from math import ceil

class Solution:
    def successfulPairs1(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []

        for spell in spells:
            arr = sorted([x * spell for x in potions])
            left, right = 0, len(arr) - 1
            res = len(arr)
            print(arr)

            while left <= right:
                mid = (left + right) // 2
                print(left, right)

                if arr[mid] >= success:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1
            print(res)
            result.append(len(arr) - res)
            print()
        return result

    def successfulPairs2(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []

        for spell in spells:
            if spell == 0:
                result.append(0)
                continue

            min_potion = ceil(success / spell)
            res = len(potions)

            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= min_potion:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1

            result.append(len(potions) - res)
        return result

solution = Solution()
spells = list(map(int, input().split()))
potions = list(map(int, input().split()))
success = int(input())

print(solution.successfulPairs1(spells, potions, success))
print()
print(solution.successfulPairs2(spells, potions, success))