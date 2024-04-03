class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0

        for price in prices: 
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(profit, maxProfit)
        return maxProfit
        
        #Time = O(n)
        #Space = O(1)