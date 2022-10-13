class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for ele in coins:
                if i - ele >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-ele])
        print(dp)
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
        