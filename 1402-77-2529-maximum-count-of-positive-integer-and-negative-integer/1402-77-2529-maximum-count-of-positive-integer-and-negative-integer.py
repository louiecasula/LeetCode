class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Keep a pos and neg variable
        pos = neg = 0
        # Sort nums and make it a set
        nums = sorted(nums)
        # Iterate nums,
        for i in range(len(nums)):
            # If num < 0, increment neg
            if nums[i] < 0:
                neg += 1
            # Elif num > 0, set pos to remaining length of nums and break
            elif nums[i] > 0:
                pos = len(nums) - i
                break
        # Return the greater value between pos & neg
        return max(pos, neg)