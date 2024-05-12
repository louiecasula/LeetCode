class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edgecase: input is empty
        if len(nums) == 0:
            return 0
        # Keep an output variable
        out = 1
        # Sort nums and remove duplicates
        nums = sorted(list(set(nums)))
        n = len(nums)
        # Iterate nums, keep track of current sequence, update output after each sequence
        seq = 1
        for i in range(n - 1):
            if nums[i + 1] == nums[i] + 1:
                seq += 1
            else:
                seq = 1
            out = max(out, seq)
        # Return output
        return out