from typing import List

"""
You are given an array prices where prices[i] 
is the price of a given stock on the ith day.

You want to maximize your profit by choosing 
a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from 
this transaction. If you cannot achieve any profit, return 0.

 
"""


class Solution:
    def method(self, prices: List[int]) -> int:
        minx = prices[0]
        resultx = 0
        for price in range(len(prices)):
            minx = min(minx, prices[price])
            resultx = max(resultx,prices[price]-minx)
        return resultx


 

solution = Solution()
test1 = [7,1,5,3,6,4] # sell on day 5, 5
test2 = [7,6,4,3,1]  # 0
test3 = [45]  # 1

result_1 = solution.method(test1)
result_2 = solution.method(test2)
result_3 = solution.method(test3)

print(result_1, result_2, result_3)
