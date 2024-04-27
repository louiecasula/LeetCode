class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Map all chars in ring by their index
        loc = defaultdict(list)
        for i, char in enumerate(ring):
            loc[char].append(i)
        # Initialize DP table with high values
        dp = [[sys.maxsize] * len(ring) for _ in range(len(key))]
        # Calculate steps from starting point to first char in key
        for x in loc[key[0]]:
            dp[0][x] = min(x, len(ring) - x) + 1
        # Fill the DP table
        for i in range(1, len(key)):
            for j in loc[key[i - 1]]:
                for k in loc[key[i]]:
                    # Calculate the shorter of the wrap-around and direct distances
                    direct = abs(k - j)
                    wrap = len(ring) - direct
                    dist = min(direct, wrap) + 1
                    # Update minimum distance up to that char
                    dp[i][k] = min(dp[i][k], dp[i - 1][j] + dist)
        # Return minimum final dp val + length of key
        return min(dp[len(key) - 1])