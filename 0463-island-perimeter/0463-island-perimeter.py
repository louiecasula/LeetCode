class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Keep a perimeter variable
        perimeter = 0
        # Iterate columns
        for i in range(len(grid)):
            # Iterate rows
            for j in range(len(grid[0])):
                # If cell == 1, increment perimeter by 4
                if grid[i][j] == 1:
                    perimeter += 4
                    # Decrement for each filled cell surrounding current
                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        perimeter -= 1
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        perimeter -= 1
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                        perimeter -= 1
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        perimeter -= 1
        # Return perimeter
        return perimeter