class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        
        l, r = 0, 1
        
        
        while l < r and r < len(prices):
            currMax = max(currMax, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return currMax