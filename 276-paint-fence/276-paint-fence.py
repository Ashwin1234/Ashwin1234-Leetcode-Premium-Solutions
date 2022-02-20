class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [[0 for i in range(n)] for j in range(3)]
        if n == 1:
            return k
        dp[0][0] = 0
        dp[1][0] = 0
        dp[2][0] = 0
        dp[0][1] = k
        dp[1][1] = k * (k-1)
        dp[2][1] = dp[0][1] + dp[1][1]
        for i in range(2,n):
            dp[0][i] = dp[1][i-1] * 1
            dp[1][i] = dp[2][i-1] * (k-1)
            dp[2][i] = dp[0][i] + dp[1][i]
        return dp[2][n-1]
        