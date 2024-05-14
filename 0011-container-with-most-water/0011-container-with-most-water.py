class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Keep an output variable and two pointers set to both sides of the array
        out = 0
        l, r = 0, len(height) - 1
        # While left is less than right,
        while l < r:
            # Multiply the lesser pointer value by the distance between pointers
            volume = min(height[l], height[r]) * (r - l)
            # Update output if a new max volume is reached
            out = max(out, volume)
            # Shift lower pointer
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        # Return output
        return out