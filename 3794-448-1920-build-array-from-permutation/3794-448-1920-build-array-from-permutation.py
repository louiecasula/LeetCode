class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Keep a prepopulated output list of length nums
        N = len(nums)
        out = [0] * N
        # Iterate nums,
        for i in range(len(nums)):
            # Set out[i] to nums[nums[i]]
            out[i] = nums[nums[i]]
        # Return output
        return out