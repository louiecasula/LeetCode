class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Find the sum of nums, nsum
        nsum = sum(nums)
        # Keep a lsum variable
        lsum = 0
        # Iterate nums,
        for i in range(len(nums)):
            # If nsum - lsum == lsum, return i
            if nsum - lsum - nums[i] == lsum:
                return i
            # Update lsum
            lsum += nums[i]
        # Else, return -1
        return -1