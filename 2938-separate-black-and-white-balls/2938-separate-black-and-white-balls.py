class Solution:
    def minimumSteps(self, s: str) -> int:
        # Keep a zCount and an output counter
        zCount = out = 0
        # Iterate s backwards,
        for i in range(len(s) -1, -1, -1):
            # If a 1 is reached, increment out by 0 count
            if s[i] == "1":
                out += zCount
            else:
                zCount += 1
        # Return output
        return out