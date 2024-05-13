class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Save lengths for row and column
        nCol = len(grid)
        nRow = len(grid[0])
        # Iterate rows,
        for row in grid:
            # If any first value is a zero, flip row
            if row[0] == 0:
                row[:] = [1 if x == 0 else 0 for x in row]
        # Iterate columns,
        for j in range(nRow):
            col = []
            for i in range(nCol):
                col.append(grid[i][j])
            # If there are more zeroes than ones, flip column
            if col.count(0) > nCol / 2:
                for i in range(nCol):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        # Return the sum of each row's value
        out = 0
        for row in grid:
            bitString = "".join([str(x) for x in row])
            out += int(bitString, 2)
        return out