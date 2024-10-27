class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Keep a cache and an output variable
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = [[-1 for x in range(COLS)] for y in range(ROWS)]
        out = 0
        # DFS function to find maximal square from given coordinate
        def dfs(r, c):
            # Base case: end of row or column reached or val is 0
            if r == ROWS or c == COLS or matrix[r][c] == 0:
                return 0
            # If coordinate already in cache, return val
            if cache[r][c] >= 0:
                return cache[r][c]
            # Recursive case: run down, down-right, and right and cache the minimum val for current coordinate + 1
            cache[r][c] = 1 + min(
                dfs(r + 1, c),
                dfs(r + 1, c + 1),
                dfs(r, c + 1)
            )
            return cache[r][c]
        # Iterate rows,
        for r in range(ROWS):
            # Iterate columns,
            for c in range(COLS):
                # Increment output by DFS function result
                out += dfs(r, c)
        # Return output
        return out