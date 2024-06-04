class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Keep an output variable
        out = 0
        # Make a counter from s
        counter = Counter(s)
        freq = sorted(list(counter.values()), reverse=True)
        HighOdd = False
        # Iterate sorted counter values,
        for f in freq:
            # If there's an odd frequency, add largest to output
            if f % 2 == 1:
                if not HighOdd:
                    out += f
                    HighOdd = True
                else:
                    out += f - 1
            # Add all even frequencies to output
            if f % 2 == 0:
                out += f
        # Return output
        return out