class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_buy)
            if prices[i] < min_buy:
                min_buy = prices[i]
        return max_profit