from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day_profit = 0
        for x in range(1, len(prices)):
            if prices[x] - prices[x - 1] > 0:
                day_profit += prices[x] - prices[x - 1]
        return day_profit
