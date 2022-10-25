class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0 for i in range(0, 2)] for j in range(len(prices))]
        dp[0][0] = -prices[0]-fee
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][1] - prices[i] - fee, dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
        
        print(dp)
        return dp[len(dp) -1][1]