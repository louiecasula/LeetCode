class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Keep a counter equal to length of s
        N = len(s)
        # Edge case: strings have different lengths
        if N != len(goal):
            return False
        # While counter > 0,
        while N > 0:
            # If s == goal, return true
            if s == goal:
                return True
            # Rotate s and decrement counter
            l = s[-1]
            s = l + s[:len(s) - 1]
            N -= 1
        return False