class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        kv = Counter(nums)
        out = []
        for k, v in kv.items():
            if v > 1:
                continue
            if v == 1:
                out.append(k)
            if len(out) == 2:
                return out