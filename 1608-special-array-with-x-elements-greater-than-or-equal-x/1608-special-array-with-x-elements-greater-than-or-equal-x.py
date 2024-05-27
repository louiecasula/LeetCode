class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Sort nums
        nums.sort()
        # Iterate 
        for x in range(1, len(nums) + 1):
            if len([i for i in nums if i >= x]) == x:
                return x
        # Else return -1
        return -1