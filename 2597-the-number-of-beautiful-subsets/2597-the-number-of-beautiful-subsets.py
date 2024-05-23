class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # Keep an output variable and sort nums
        N = len(nums)
        # Function that recursively checks all "beautiful" subsets in nums
        def beautiful(i, count):
            # Base case: all subsets have been run
            if i == N:
                return 1
            # Recursive case: increment output for each diff that isn't k
            res = beautiful(i + 1, count)
            if not count[nums[i] + k] and not count[nums[i] - k]:
                count[nums[i]] += 1
                res += beautiful(i + 1, count)
                count[nums[i]] -= 1
            return res
        # Return result of function 
        return beautiful(0, defaultdict(int)) - 1