class Solution:
    def trap(self, height: List[int]) -> int:
        # If length of height is less than 3, return 0
        if len(height) < 3:
            return 0
        # Keep an output counter and a left and right max
        out = 0
        # Iterate,
        for i in range(len(height)):
        # Find max height to left and right of element
            left = max(height[:i]) if i > 0 else 0
            right = max(height[i + 1:]) if i < len(height) - 1 else 0
            # Increment output by min of max heights - current height
            water = min(left, right) - height[i]
            if water > 0:
                out += water
        # Return output
        return out