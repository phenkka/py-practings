class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        a, b = len(str1), len(str2)
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return str1[:a + b]

solution = Solution()
str1= input()
str2 = input()

print(solution.gcdOfStrings(str1, str2))