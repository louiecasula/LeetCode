class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Return the sum of every digit in start XOR goal
        return sum([eval(i) for i in list("{0:b}".format(start ^ goal))])