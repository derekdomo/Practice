"""
You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot 
achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must 
buy before you sell.
"""


class Solution:
    def solve(self, stocks):
        max_profit = 0
        for i, price in enumerate(stocks):
            for j in range(i+1, len(stocks)):
                max_profit = max(max_profit, stocks[j] - price)

        return max_profit
    
    def solve_opt(self, stocks):
        max_profit = 0
        min_stock_price = stocks[0]
        for stock in stocks[1:]:
            if stock < min_stock_price:
                min_stock_price = stock
            else:
                max_profit = max(stock - min_stock_price, max_profit)

        return max_profit


sol = Solution()
r = sol.solve_opt([7,1,5,3,6,4])
print(r)
