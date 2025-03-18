class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        hash_map = {}

        for letter in s:
            hash_map[letter] = hash_map.get(letter, 0) + 1

        for letter in t:
            if letter not in hash_map or hash_map[letter] == 0:
                return False
            hash_map[letter] -= 1

        return True

solution = Solution()

s = input()
t = input()

print(solution.isAnagram(s, t))