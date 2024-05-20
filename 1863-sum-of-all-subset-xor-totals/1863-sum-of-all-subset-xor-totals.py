class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Keep an output variable
        out = 0
        N = len(nums)
        # Find all subsets and add their XOR value to output
        for i in range(1 << N):
            x = 0
            for j in range(N):
                if ((i >> j) & 1) != 0:
                    x ^= nums[j]
            out += x
        # Return output
        return out