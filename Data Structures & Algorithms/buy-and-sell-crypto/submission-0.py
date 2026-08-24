class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_low = prices[0]
        p = 0

        for i in prices:
            if i < buy_low:
                buy_low = i

            p = max(p, i - buy_low)
        
        return p
        