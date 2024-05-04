class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keep a frequency hashtable, a left and right pointer, and a counter variable
        out = 0
        freq = defaultdict(int)
        l = 0
        # While shifting right, shift left if any frequency is greater than 1
        for r in range(len(s)):
            freq[s[r]] += 1
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            out = max(out, r - l + 1) 
        # Return counter
        return out