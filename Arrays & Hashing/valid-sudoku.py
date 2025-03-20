from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]):
        for row in board:
            numbers = [num for num in row if num != "."]
            if len(numbers) != len(set(numbers)):
                return False

        for col in zip(*board):
            numbers = [num for num in col if num != "."]
            if len(numbers) != len(set(numbers)):
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = set()

                for x in range(3):
                    for y in range(3):
                        num = board[row + x][col + y]
                        if num != ".":
                            if num in square:
                                return False
                            square.add(num)

        return True


solution = Solution()
board = [list(input().split()) for _ in range(9)]

print(solution.isValidSudoku(board))