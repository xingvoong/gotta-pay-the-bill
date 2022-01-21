"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day

On each day, you may decide to buy and/or sell the stock.  You can only hold at most one share of the stock at any time.  However, you can buy it then immedidately sell it on the same day.

Find and return the maxinum profit you can achieve.

Exampl 1:

input: prices = [7, 1, 5, 3, 6, 4]
Output: 7
Explanation: buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.

Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6 - 3 = 3
Total profit is 4 + 3 = 7

Example 2:

input: prices = [1, 2, 3, 4, 5]
Output: 4
Explanation: buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5 - 1 = 4
Total profit is 4.

Example 3:
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: there is no way to make a positive profit, so we never buy the stock to achieve the maxinum profit of 0

for each them, compare the price today with the price the day before to see whether
the price go up.  Since we can buy and sell multiple days.  we can just keep buying and selling them.
"""


def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit


example1 = [7, 1, 5, 3, 6, 4]
example2 = [7, 6, 4, 3, 1]

print(maxProfit(example2))

"""
time: O(N)
space: O(1)
"""
