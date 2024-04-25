class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Keep a set of letters and a dp dict
        char_set = set(s)
        dp = {}
        # For each letter in string, make an adjacency list given k only including other letters in string
        adj = defaultdict(list)
        for c in s:
            if c not in adj:
                for i in range(1, k + 1):
                    if chr(ord(c) + i) in char_set:
                        adj[c].append(chr(ord(c) + i))
                    if chr(ord(c) - i) in char_set:
                        adj[c].append(chr(ord(c) - i))
            dp[c] = max(dp.get(adj_c, 0) + 1 for adj_c in [c] + adj[c])              
        # Return longest length in adjacency list using dp
        return max(dp.values())