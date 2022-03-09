class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for ele in prices:
            if ele < min_price:
                min_price = ele
            if ele - min_price > max_profit:
                max_profit = ele - min_price
        return max_profit