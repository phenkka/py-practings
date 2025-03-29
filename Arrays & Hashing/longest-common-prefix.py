from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        prefix = strs[0]

        for index in range(1, len(strs)):
            while strs[index][:len(prefix)] != prefix:
                prefix = prefix[:-1]

        return prefix

solution = Solution()
strs = list(map(int, input().split()))

print(solution.longestCommonPrefix(strs))