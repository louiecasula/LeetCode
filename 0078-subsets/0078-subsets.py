class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Keep an output array
        out = [[]]
        # Helper function to recursively add each subset
        def helper(index, nums, sub):
            nonlocal out
            for i in range(index, len(nums)):
                helper(i + 1, nums, sub + [nums[i]])
                out.append(sub + [nums[i]])
        # Run helper function and return output
        helper(0, nums, [])
        return out