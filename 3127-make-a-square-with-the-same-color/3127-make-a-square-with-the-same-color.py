class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        # Directions for BFS
        dRow = [0, 1, 0, 1]
        dCol = [0, 0, 1, 1]
        # BFS function that checks E, SE, and S colors and returns an int value
        def bfs(row, col):
            comp = 0
            for i in range(4):
                cR = row + dRow[i]
                cC = col + dCol[i]
                if grid[cR][cC] == "B":
                    comp += 1
                else:
                    comp -= 1
            return comp
        for i in range(len(grid) - 1):
            for j in range(len(grid[0]) - 1):
                comp = bfs(i, j)
                if comp >= 2 or comp <= -2:
                    return True
        return False