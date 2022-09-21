class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprice = 0
        for ele in prices:
            if ele < minprice:
                minprice = ele
            maxprice = max(maxprice, ele - minprice)
        return maxprice