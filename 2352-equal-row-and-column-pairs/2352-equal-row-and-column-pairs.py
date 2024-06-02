class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Keep an output variable
        out = 0
        N = len(grid)
        # Rotate grid counter-clockwise AKA save columns matrix
        cols = [[grid[j][i] for j in range(N)] for i in range(N - 1, -1, -1)]
        # Iterate grid,
        for i in range(N):
            for j in range(N):
                # If row == column, increment output
                if grid[i] == cols[j]:
                    out += 1
        # Return output
        return out