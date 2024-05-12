class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # Keep an output matrix of size n-2 x n-2
        n = len(grid)
        out = [[1 for x in range(n - 2)] for y in range(n - 2)]
        # Keep an orientation list
        direction = [-1, 0, 1]
        # Traverse matrix from [1,1] -> [n-2,n-2]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                # Append max of surrounding cells to output
                cells = [grid[i + x][j + y] for x in direction for y in direction]
                out[i - 1][j - 1] = max(cells)
        # Return output
        return out