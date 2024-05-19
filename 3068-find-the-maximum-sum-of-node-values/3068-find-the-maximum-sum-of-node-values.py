class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # Keep an output variable set to the sum of input array
        out = sum(nums)
        N = len(nums)
        # Keep a delta array of every array value XORed by k, then sort
        delta = [(x ^ k) - x for x in nums]
        delta.sort(reverse=True)
        # Iterate delta values two at a time,
        for i in range(0, N, 2):
            # Break after the last even indexed value
            if i == N - 1:
                break
            # Break if the two deltas' sum is 0 or lower
            delta_sum = delta[i] + delta[i + 1]
            if delta_sum <= 0:
                break
            # Otherwise, add values to output variable
            out += delta_sum
        # Return output variable
        return out