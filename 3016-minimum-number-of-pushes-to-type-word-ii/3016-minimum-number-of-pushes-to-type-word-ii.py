class Solution:
    def minimumPushes(self, word: str) -> int:
        # Keep an output variable
        out = 0
        # Map frequency of each char
        freq = defaultdict(int)
        for c in word:
            freq[c] += 1
        # Sort map by frequency in descending order,
        freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        # Iterate map,
        for i, f in enumerate(freq.values()):
            # If 0 <= i <= 7, increment output by values
            if 0 <= i <= 7:
                out += f
            # If 8 <= i <= 15, increment output by 2 x values
            elif 8 <= i <= 15:
                out += 2 * f
            # If 16 <= i <= 23, increment output by 3 x values
            elif 16 <= i <= 23:
                out += 3 * f
            # Else, increment output by 4 x values
            else:
                out += 4 * f
        # Return output
        return out