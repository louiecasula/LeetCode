class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Keep an output array
        out = []
        N = len(nums)
        # Sort nums
        nums.sort()
        # Iterate from i -> N - 2,
        for i in range(N - 2):
            # Stop early if i is greater than 0
            if nums[i] > 0:
                break
            # Avoid duplicate i values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Keep two additional pointers
            j, k = i + 1, N - 1
            # While j is less than k,
            while j < k:
                # Save sum of all pointer values
                currSum = nums[i] + nums[j] + nums[k]
                # If sum is less than 0, increment j
                if currSum < 0:
                    j += 1
                # If sum is more than 0, decrement k
                elif currSum > 0:
                    k -= 1
                # If sum equals 0, add it to output and increment j
                else:
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Continue moving j if its value is the same
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        # Return output
        return out