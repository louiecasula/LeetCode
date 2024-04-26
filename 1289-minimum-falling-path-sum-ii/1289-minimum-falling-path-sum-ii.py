class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Edgecase: n == 1
        if len(grid) == 1:
            return grid[0][0]
        # Keep a dp matrix
        dp = grid
        # Starting from second row, set dp cells to the shortest path to it + cell val
        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                dp[i][j] = grid[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])
        # Return minimum final dp row val
        return min(dp[len(dp) - 1])