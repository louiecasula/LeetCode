class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Keep an output variable
        out = 0
        N = len(nums)
        # Iterate nums to len - 2,
        for i in range(N - 2):
            # If num is 0, flip window, increment output
            if nums[i] == 0:
                for j in range(3):
                    nums[i + j] = 0 if nums[i + j] == 1 else 1
                out += 1
        # If nums is all 1s, return out
        if nums == [1] * N:
            return out
        # Else, return -1
        return -1