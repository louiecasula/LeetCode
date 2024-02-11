class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort array
        nums.sort()
        # Return element at the midpoint
        return nums[int(len(nums)/2)]