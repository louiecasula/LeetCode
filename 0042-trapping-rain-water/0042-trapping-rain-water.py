class Solution:
    def trap(self, height: List[int]) -> int:
        # Keep an output counter, left and right pointers, and left and right maxes
        out = 0
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        # Iterate,
        while l < r:
            # Sum the lesser of lmax and rmax - l or r
            # If the sum is positive, add to output
            # Update whichever max was target
            # Move the pointer that had the lesser max
            if rmax < lmax:
                r -= 1
                rmax = max(rmax, height[r])
                out += rmax - height[r]
            else:
                l += 1
                lmax = max(lmax, height[l])
                out += lmax - height[l]
        # Return output
        return out