class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthiest = 0 
        for amount in accounts: 
            curr_wealth = sum(amount)
            wealthiest = max(curr_wealth, wealthiest)
        return wealthiest

        