class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        out = -1
        for num in nums:
            if num > 0 and (num * -1) in nums and num > out:
                out = num
        return out