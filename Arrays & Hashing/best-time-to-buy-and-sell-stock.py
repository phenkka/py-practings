from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 100000000

        for price in prices:
            if price < min_price:
                min_price = price

            current_profit = price - min_price
            if current_profit > profit:
                profit = current_profit

        return profit

solution = Solution()
prices = list(map(int, input().split()))

print(solution.maxProfit(prices))