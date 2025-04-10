from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        all_nums = set1 | set2

        return [list(all_nums - set2), list(all_nums - set1)]

solution = Solution()
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(solution.findDifference(nums1, nums2))