class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Keep an output variable
        out = 0
        total = 0
        # Map the running sum % k to the count of that remainder
        rem = {0: 1}
        for num in nums:
            total += num
            r = total % k
            if r in rem:
                out += rem[r]
                rem[r] += 1
            else:
                rem[r] = 1
        # Return output
        return out