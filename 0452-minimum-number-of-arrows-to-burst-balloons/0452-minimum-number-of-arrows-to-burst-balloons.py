class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Edgecase(s)
        if len(points) == 1: 
            return 1
        # Sort the points by the starts (with priority on the lengths?)
        points = sorted(points)
        # Keep a counter, maxStart = first bal's start, minEnd = first bal's end
        count = 1
        maxStart = points[0][0]
        minEnd = points[0][1]
        # Iterate starting from second balloon,
        for i in range(1, len(points)):
            # If curr bal's start >= minEnd, make maxStart & minEnd curr bal's values, increment counter
            if points[i][0] > minEnd:
                count += 1
                maxStart = points[i][0]
                minEnd = points[i][1]
            # Else, update maxStart & minEnd
            else:
                maxStart = max(maxStart, points[i][0])
                minEnd = min(minEnd, points[i][1])
        # Return counter
        return count