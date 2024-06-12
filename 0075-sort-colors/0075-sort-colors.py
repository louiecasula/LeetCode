class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Keep pointer, l
        l = 0
        # From 0 -> 2,
        for color in range(3):
            # Iterate nums,
            for i in range(l, len(nums)):
                # If num == i, swap with l pointer and increment l
                if nums[i] == color:
                    temp = nums[i]
                    nums[i] = nums[l]
                    nums[l] = temp
                    l += 1
