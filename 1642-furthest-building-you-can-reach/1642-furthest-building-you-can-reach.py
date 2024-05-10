class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Keep a priority queue
        pq = []
        # Iterate through the buildings
        for i in range(len(heights) - 1):
            # Calculate difference in height between buildings, continue if negative or 0
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            # Subtract difference from bricks, push difference to pq
            bricks -= diff
            heapq.heappush(pq, -diff)
            # If bricks are negative, add highest difference from pq to bricks and decrement ladders
            if bricks < 0:
                bricks += -heapq.heappop(pq)
                ladders -= 1
            # If ladders are negative, return current index
            if ladders < 0:
                return i
        # Return length of list - 1
        return len(heights) - 1