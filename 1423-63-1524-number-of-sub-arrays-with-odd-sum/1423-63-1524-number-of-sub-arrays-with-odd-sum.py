class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Keep an odd and a prefix sum variable
        odd = psum = 0
        # Iterate arr,
        for num in arr:
            # Increment psum by num and increment odd by half of psum
            psum += num
            odd += psum % 2
        # Return odd + odd * even
        return odd + odd * (len(arr) - odd) % (10 ** 9 + 7)