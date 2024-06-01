class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Keep an output variable and two pointers, left and right, set to first and last element
        out = 0
        l, r = 0, len(nums) - 1
        # Sort nums
        nums.sort()
        # While pointers don't equal eachother,
        while l < r:
            psum = nums[l] + nums[r]
            # If sum of pointer vals > k, decrement r
            if psum > k:
                r -= 1
            # Else if sum < k, increment l
            elif psum < k:
                l += 1
            # Else (sum == k), increment output and move both pointers
            else:
                out += 1
                l += 1
                r -= 1
        # Return output
        return out