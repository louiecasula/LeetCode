class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        # Keep an output variable and count of 1s in each row and col
        out = 0
        rowOnes = [sum(x) for x in grid]
        colOnes = [sum(grid[x][y] for x in range(len(grid))) for y in range(len(grid[0]))]
        # Iterate rows,
        for i in range(len(rowOnes)):
            # Iterate cols,
            for j in range(len(colOnes)):
                # Add num 1s in row - 1 * num 1s in col - 1 to output
                if grid[i][j] == 1:
                    out += (rowOnes[i] - 1) * (colOnes[j] - 1)
        # Return output
        return out