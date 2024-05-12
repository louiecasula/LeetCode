class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            all_nums = []
            for num in row:
                if num.isnumeric():
                    all_nums.append(num)
            no_dup = set(all_nums)
            if len(all_nums) != len(no_dup):
                return False
        # Check columns
        for j in range(9):
            all_nums = []
            for i in range(9):
                if board[i][j].isnumeric():
                    all_nums.append(board[i][j])
            no_dup = set(all_nums)
            if len(all_nums) != len(no_dup):
                return False
        # Check each 3x3 grid
        grids = [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]
        directions = [-1, 0, 1]
        for grid in grids:
            i, j = grid[0], grid[1]
            all_nums = [board[i + x][j + y] for x in directions for y in directions if board[i + x][j + y].isnumeric()]
            no_dup = set(all_nums)
            if len(all_nums) != len(no_dup):
                return False
        # Return true if board passes all checks
        return True