class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # While length of nums is greater than 1,
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            # If middle num < target, set l to mid + 1
            if nums[mid] < target:
                l = mid + 1
            # Elif middle num > target, set r to mid - 1
            elif nums[mid] > target:
                r = mid - 1
            # Else, return middle index
            else:
                return mid
        # Return -1
        return -1