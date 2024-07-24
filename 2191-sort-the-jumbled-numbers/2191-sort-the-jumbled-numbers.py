class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # Iterate nums,
        N = len(nums)
        for i in range(N):
            # Map each num to its new mapping val
            temp = ""
            s = str(nums[i])
            for d in s:
                temp = temp + str(mapping[int(d)])
            nums[i] = (int(temp), i, nums[i])
        # Sort nums by new mapped val
        nums.sort()
        # Return list comp of original nums
        return [x[2] for x in nums]