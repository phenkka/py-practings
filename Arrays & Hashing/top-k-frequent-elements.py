from typing import List
from collections import Counter

class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        mhash = {}

        for num in nums:
            mhash[num] = mhash.get(num, 0) + 1

        sort_mhash = dict(sorted(mhash.items(), key=lambda x: x[1], reverse=True))
        return list(sort_mhash.keys())[:k]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        mhash = Counter()

        for num in nums:
            mhash[num] += 1

        return list(dict(mhash.most_common(k)).keys())

solution = Solution()

nums = list(map(int, input().split()))
k = int(input())

print(f"First solution - {solution.topKFrequent1(nums, k)}")
print()
print(f"Second solution - {solution.topKFrequent2(nums, k)}")