class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(0,n):
            dp[0][i] = matrix[0][i]
        for i in range(1,m):
            for j in range(0,n):
                if j==0:
                    dp[i][j] = min(dp[i-1][j] , dp[i-1][j+1]) + matrix[i][j]
                elif j==n-1:
                    dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1]) + matrix[i][j]
                else:   
                    dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1] , dp[i-1][j + 1]) + matrix[i][j]
        
        return min(dp[m-1])
            
                
                
        