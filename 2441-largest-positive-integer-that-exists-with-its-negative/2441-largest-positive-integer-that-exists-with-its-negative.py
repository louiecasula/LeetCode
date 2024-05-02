class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        out = -1
        for num in nums:
            if num > 0 and -num in nums:
                out = max(out, num)
        return out