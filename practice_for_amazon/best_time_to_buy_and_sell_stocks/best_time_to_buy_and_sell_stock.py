"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

# having a variable min_price
# and a max_profit
# at every step, we calculate the profit in respect with the min price and the current price
# [7, 1, 5, 3, 6, 4]
def max_profit(prices):
    max_profit = 0
    min_price = prices[0]
    for p in prices:
        min_price = min(p, min_price)
        max_profit = max(max_profit, p - min_price)

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))

"""
time: O(N)
space: O(1)
"""
