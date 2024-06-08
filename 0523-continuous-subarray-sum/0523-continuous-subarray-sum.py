class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Keep a map and a currSum variable
        rem = {0: -1}
        currSum = 0
        # Iterate nums,
        for i, n in enumerate(nums):
            # Update currSum, calculate mod val by k
            currSum += n
            mod = currSum % k
            # If mod val isn't in map, add it as a key with i as val
            if mod not in rem:
                rem[mod] = i
            # Else if the difference in indeces is greater than 1, return true
            elif i - rem[mod] > 1:
                return True
        # Return false
        return False