# dp

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = float('inf')
        
        for price in prices:
            maxProfit = max(maxProfit,price - minPrice)
            minPrice = min(price, minPrice)
        return maxProfit
