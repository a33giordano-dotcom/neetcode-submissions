class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = l = 0

        for i in range(1, len(prices)):
            if (prices[i] - prices[l] < 0):
                l = i
                res = max(res, 0)
            res = max(res, prices[i] - prices[l])

        return res    