class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Keep an output variable and psum variable
        out, psum = 0, 0
        # Increment psum by each val in gain, update output each time
        for g in gain:
            psum += g
            out = max(out, psum)
        # Return output
        return out