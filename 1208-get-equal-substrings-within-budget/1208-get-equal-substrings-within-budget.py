class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Find the difference between s and t at each index
        N = len(s)
        diff = [0] * N
        # Keep a variable to count diffs greater than maxCost
        high = 0            
        # Return the length of the longest difference subarray that sums to maxCost
        out = 0
        l = 0
        cost = 0
        for r in range(N):
            diff[r] = abs(ord(s[r]) - ord(t[r]))
            if diff[r] > maxCost:
                high += 1
            cost += diff[r]
            while cost > maxCost and l < r:
                cost -= diff[l]
                l += 1
            out = max(out, r - l + 1)
        # If all diffs are greater than maxCost, return 0
        if high == N:
            return 0
        return out