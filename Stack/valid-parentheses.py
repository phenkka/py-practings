class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for element in s:
            if element in "([{":
                stack.append(element)
            else:
                try:
                    bracket = stack.pop()
                except:
                    return False

                if element == ")" and bracket == "(":
                    continue
                if element == "]" and bracket == "[":
                    continue
                if element == "}" and bracket == "{":
                    continue
                return False

        if len(stack) > 0:
            return False
        return True

solution = Solution()
s = input()

print(solution.isValid(s))