class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Add nums to counter
        kv = Counter(nums)
        # Iterate counter kv pairs, if value == 1, return key
        for k, v in kv.items():
            if v == 1:
                return k