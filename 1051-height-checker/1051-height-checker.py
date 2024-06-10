class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Make a copy of heights and sort
        sortHeights = sorted([x for x in heights])
        # Keep an output variable
        out = 0
        # Iterate and increment output for each different value in both lists
        for i in range(len(heights)):
            if heights[i] != sortHeights[i]:
                out += 1
        # Return output
        return out
        