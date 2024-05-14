class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # Keep an output variable
        out = 0
        # Make a function that recursively checks paths in every direction
        def recursion(si, sj, nGrid, gold):
            directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
            gold += nGrid[si][sj]
            maxGold = gold
            # Recursive case: move to a surrounding cell
            for x, y in directions:
                if 0 <= si + x < len(nGrid) and 0 <= sj + y < len(nGrid[0]) and nGrid[si + x][sj + y] != 0:
                    newGrid = [row[:] for row in nGrid]
                    newGrid[si][sj] = 0
                    maxGold = max(maxGold, recursion(si + x, sj + y, newGrid, gold))
            return maxGold
        # Iterate grid, if cell isn't 0, run recursive function
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    out = max(out, recursion(i, j, grid, 0))
        # Return output
        return out