class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Keep two variables for first two triplet numbers
        f = s = sys.maxsize
        # Iterate from third element to end
        for t in nums:
            if t <= f:
                f = t
            elif t <= s:
                s = t
            else:
                return True
        # Return False
        return False