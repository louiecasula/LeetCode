class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Keep an output variable
        out = 0
        # Iterate nums,
        for i in range(1, len(nums)):
            # While curr < prev, increment curr and output
            if nums[i] <= nums[i - 1]:
                out += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        # Return output
        return out