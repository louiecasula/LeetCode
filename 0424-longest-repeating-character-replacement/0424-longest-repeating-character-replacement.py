class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Keep an output variable, two pointers, a freq dict, and a maxFreq variable
        out = 1
        l, r = 0, 0
        freq = defaultdict(int)
        maxFreq = 0
        # While right pointer is less than final index,
        while r < len(s):
            # Update freq and maxFreq
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            # If length of current substring - freq of mainChar > k, update freq and shift left pointer
            if r - l + 1 - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            # Else, update output and shift right pointer
            out = max(out, r - l + 1)
            r += 1
        # Return output
        return out