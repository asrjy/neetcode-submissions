class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        best_profit = -1
        for i in range(1, len(prices)):
            min_buy = min(min_buy, prices[i-1])
            best_profit = max(prices[i] - min_buy, best_profit)
        return max(best_profit, 0)
