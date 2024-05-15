class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # Save the length and keep an array of directions and a queue
        N = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        # Helper function to check if cell is in bounds
        def inside_bounds(r, c):
            return 0 <= r < N and 0 <= c < N
        # Iterate grid, if cell is 1, add to queue
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    grid[i][j] = 0
                    q.append((0, i, j))
                else:
                    grid[i][j] = inf
        # For each thief in queue, find distance to next thief
        while q:
            d, i, j = q.popleft()
            for dx, dy in directions:
                if inside_bounds(i + dx, j + dy) and grid[i + dx][j + dy] == inf:
                    row, col = i + dx, j + dy
                    grid[row][col] = d + 1
                    q.append((d + 1, row, col))
        # Keep a "max heap" and a visited set
        max_heap = [(-grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        # For each cell in heap,
        while max_heap:
            d, i, j = heapq.heappop(max_heap)
            d = -d # Reverse distance val (bc Python...)
            # If the end is reached, return distance
            if i == N - 1 and j == N - 1:
                return d
            # Check surrounding cells, adding them and their distance to heap
            for dx, dy in directions: 
                if inside_bounds(i + dx, j + dy) and (i + dx, j + dy) not in visited:
                    (row, col) = (i + dx, j + dy) 
                    visited.add((row, col))
                    min_d = min(d, grid[row][col])
                    heapq.heappush(max_heap, (-min_d, row, col))