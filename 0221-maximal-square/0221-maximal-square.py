class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        max_area = -1
        for i in range(0, len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
        
        for i in range(0, len(matrix)):
            dp[i][0] = int(matrix[i][0])
            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        
        for i in range(0, len(dp)):
            for j in range(0, len(dp[0])):
                max_area = max(dp[i][j], max_area)
        
        return max_area * max_area