import re

class Solution:
    def reverseVowels(self, s: str) -> str:
        pattern = "aeiouAEIOU"
        s = list(s)

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in pattern and s[right] in pattern:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in pattern and s[right] not in pattern:
                right -= 1
            elif s[left] not in pattern and s[right] in pattern:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(s)

solution = Solution()
s = input()

print(solution.reverseVowels(s))