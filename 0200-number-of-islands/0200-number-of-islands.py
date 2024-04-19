class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edgecase
        if not grid:
            return 0
        # Keep row & column lengths, a visited set (of tuples), and an output counter
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        # DFS function to check all adjacent cells
        def dfs(r, c):
            # Keep a stack
            stack = [(r, c)]
            # Mark the starting cell as visited
            visited.add((r, c))
            while stack:
                row, col = stack.pop()
                # Check all four possible directions
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = row + dr, col + dc
                    # Check boundaries and if the new cell is land and not visited
                    if (0 <= new_row < rows and 0 <= new_col < cols and
                            grid[new_row][new_col] == '1' and (new_row, new_col) not in visited):
                        stack.append((new_row, new_col))
                        visited.add((new_row, new_col))
        # Traverse matrix,
        for r in range(rows):
            for c in range(cols):
                # If a cell is land and not visited, apply dfs and increment islands
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        # Return number of islands
        return islands
