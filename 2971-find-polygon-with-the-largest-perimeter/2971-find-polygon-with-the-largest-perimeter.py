class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort nums in desc order
        nums.sort(reverse = True)
        # Iterate while there are at least 3 nums
        for i in range(len(nums) - 2):
            # If current < the sum of the remaining smaller sides,
            if nums[i] < sum(nums[i + 1:]):
                # Return the sum of remaining sides
                return sum(nums[i:])
        # Return -1
        return -1