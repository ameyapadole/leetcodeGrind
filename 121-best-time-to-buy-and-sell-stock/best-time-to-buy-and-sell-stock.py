class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0 
        minprice = float('inf')

        for price in prices: 
            minprice = min(minprice, price)
            profit = price - minprice
            maxprofit = max(maxprofit, profit)
        return maxprofit

        #Time Complexity = O(N)
        #Space Complexity = O(1)        