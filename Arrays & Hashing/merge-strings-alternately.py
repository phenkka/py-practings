class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        result = []

        for index in range(min_len):
            result.append(word1[index])
            result.append(word2[index])

        result.append(word1[min_len:])
        result.append(word2[min_len:])

        return "".join(result)

solution = Solution()
word1 = input()
word2 = input()

print(solution.mergeAlternately(word1, word2))