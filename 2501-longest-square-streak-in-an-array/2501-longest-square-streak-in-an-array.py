class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Keep a map and an output variable
        streaks = {}
        out = -1
        # Sort nums
        nums.sort()
        # Iterate nums,
        for num in nums:
            # If num's int square root == square root and int square root in map,
            sqr = isqrt(num)
            if sqr * sqr == num and sqr in streaks:
                # Set nums's val to int square root's val + 1
                streaks[num] = streaks[sqr] + 1
                # Update output with greater of values
                out = max(out, streaks[num])
            # Else, set num's val to 1
            else:
                streaks[num] = 1
        # Return output
        return out