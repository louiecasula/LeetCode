class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Square each number in the array
        for i in range(len(nums)):
            nums[i] *= nums[i]
        # Return sorted array
        return sorted(nums)