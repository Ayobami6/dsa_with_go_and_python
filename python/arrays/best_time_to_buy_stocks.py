#!/usr/bin/python3
from typing import List
"""
Best time to buy stock
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. However, 
you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""


def best_time_to_buy_stocks(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            profit = prices[i + 1] - prices[i]
            max_profit += profit
    return max_profit


prices = [7, 1, 5, 3, 6, 4]

print(best_time_to_buy_stocks(prices))
