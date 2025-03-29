class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

solution = Solution()
s = input()

print(solution.lengthOfLastWord(s))