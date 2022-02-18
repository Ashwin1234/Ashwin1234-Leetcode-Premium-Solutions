class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        dp = [0] * n
        dp[0] = 0
        if amount == 0:
            return 0
        for i in range(1,n):
            min1 = float('inf')
            for j in range(0,len(coins)):
                if coins[j] <= i:
                    if i-coins[j] == 0 or dp[i-coins[j]] > 0:
                        min1 = min(min1,dp[i-coins[j]] + 1)
            if min1 < float('inf'):
                dp[i] = min1
        print(dp)
        if dp[amount] > 0:
            return dp[amount]
        else:
            return -1
        