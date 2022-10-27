class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n):
            max_val = -1
            for j in range(1, i):
                max1 = dp[j] * dp[i-j]
                max_val = max(i, max_val, max1)
            dp[i] = max_val
        max_val = -1
        for j in range(1, n):
            max1 = dp[j] * dp[n-j]
            max_val = max(max_val, max1)
        print(dp)
        dp[n] = max_val
        return dp[n]