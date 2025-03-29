class Solution:
    def reverseWords(self, s: str) -> list:
        list_s = s.strip().split(" ")
        result = ""

        for word in list_s:
            if word:
                result = " " + word + result
            continue
        return result.strip()

solution = Solution()
s = input()

print(solution.reverseWords(s))