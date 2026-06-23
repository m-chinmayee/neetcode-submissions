class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [8, 3, 4, 6, 4, 7, 1, 7]
        if len(prices) == 0 or len(prices) == 1:
            return 0

        profit = 0
        i = 1
        min = prices[0]
        while i < len(prices):
            if (prices[i]-min) >= profit:
                profit = prices[i] - min
            elif prices[i] < min:
                min = prices[i]
            i += 1
        
        return profit