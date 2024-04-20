class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # Keep length variables, a farmland array, a visited set
        rows, cols = len(land), len(land[0])
        farmland = []
        visited = set()
        # Function to mark all cells in a rectangle as visited
        def mark_visited(x1, y1, x2, y2):
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    visited.add((i, j))
        # Traverse matrix
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    # Find the rightmost boundary
                    right = j
                    while right + 1 < cols and land[i][right + 1] == 1:
                        right += 1
                    # Find the bottommost boundary
                    bottom = i
                    while bottom + 1 < rows and land[bottom + 1][j] == 1:
                        bottom += 1
                    # Mark all cells in the rectangle as visited
                    mark_visited(i, j, bottom, right)
                    # Append the top-left and bottom-right corners of the rectangle
                    farmland.append([i, j, bottom, right])
        # Return farmland
        return farmland