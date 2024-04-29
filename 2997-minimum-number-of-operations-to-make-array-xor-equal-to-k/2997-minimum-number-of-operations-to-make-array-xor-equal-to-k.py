class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Do XOR operation on each num in nums
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        xor ^= k
        # Add to output for each different bit between xor and k
        out = 0
        while xor > 0:
            out += xor % 2
            xor //= 2
        return out