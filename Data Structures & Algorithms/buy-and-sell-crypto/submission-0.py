class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        yes = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r+=1
            else:
                r+=1 
            yes = max(profit, yes)
        return yes 

        