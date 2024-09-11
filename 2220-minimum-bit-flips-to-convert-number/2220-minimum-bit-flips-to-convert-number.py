class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Return the sum of every digit in start XOR goal
        return "{0:b}".format(start ^ goal).count("1")