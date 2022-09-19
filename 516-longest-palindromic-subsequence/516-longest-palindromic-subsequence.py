class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(0, len(s)):
            dp[i][i] = 1
        for i in range(1, len(s)):
            for j in range(0, len(s) - i):
                k = j + i
                if s[j] == s[k]:
                    dp[j][k] = dp[j][k] + 2 + dp[j+1][k-1]
                else:
                    dp[j][k] = max(dp[j][k-1], dp[j+1][k])
        
        return dp[0][len(s) - 1]
                
        