class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # If nums is 4 or less numbers, return 0
        if len(nums) < 5:
            return 0
        # Sort nums, return difference between first and fourth from last nums
        nums.sort()
        return min(abs(nums[0] - nums[-4]), abs(nums[1] - nums[-3]), abs(nums[2] - nums[-2]), abs(nums[3] - nums[-1]))