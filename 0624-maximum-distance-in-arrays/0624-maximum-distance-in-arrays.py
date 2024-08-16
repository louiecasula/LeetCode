class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Keep an output variable and a min and max val set to first array's first and last vals
        low, high, out = arrays[0][0], arrays[0][-1], 0
        # Iterate arrays from second onward,
        for i in range(1, len(arrays)):
            # Update output variable
            out = max(out, abs(high - arrays[i][0]), abs(low - arrays[i][-1]))
            # Update low and high
            low, high = min(low, arrays[i][0]), max(high, arrays[i][-1])
        # Return out
        return out