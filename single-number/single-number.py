class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for num in s:
            if nums.count(num) == 1:
                return num