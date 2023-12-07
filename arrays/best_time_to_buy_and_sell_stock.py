# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Time complexity: O(n)
# Space complexity: O(1)
# Trick: Keep track of the minimum price and the maximum profit
from typing import List


def maxProfit(prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit