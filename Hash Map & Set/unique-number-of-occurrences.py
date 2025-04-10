from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences1(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        result = []

        for key, value in cnt.items():
            result.append(value)

        if len(result) == len(set(result)):
            return True
        return False

    def uniqueOccurrences2(self, arr: List[int]):
        hash = {}
        for num in arr:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        result = []
        for key, value in hash.items():
            result.append(value)

        if len(result) == len(set(result)):
            return True
        return False


solution = Solution()
arr = list(map(int, input().split()))

print(solution.uniqueOccurrences1(arr))
print()
print(solution.uniqueOccurrences2(arr))