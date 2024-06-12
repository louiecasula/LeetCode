class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Keep pointers for start, end, and iteration
        l = i = 0
        r = len(nums) - 1
        # While iterating pointer <= end pointer,
        while i <= r:
            # Swap current num if it's a 0 or 2 with start or end pointer
            if nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                if nums[i] == 0:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
                # Increment iterating pointer
                i += 1