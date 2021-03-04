from typing import List


class Solution:
    """
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    """
    def maxProfit(self, prices: List[int]) -> int:
        day_profit = 0
        for x in range(1, len(prices)):
            if prices[x] - prices[x - 1] > 0:
                day_profit += prices[x] - prices[x - 1]
        return day_profit
