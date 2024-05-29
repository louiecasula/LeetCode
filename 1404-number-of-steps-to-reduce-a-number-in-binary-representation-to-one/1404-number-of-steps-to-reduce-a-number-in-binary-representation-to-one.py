class Solution:
    def numSteps(self, s: str) -> int:
        # Keep an output variable
        out = 0
        # Convert binary string to an integer
        binInt = int(s, 2)
        # While num isn't 1,
        while binInt != 1:
            # If num is even, half it
            if binInt % 2 == 0:
                binInt = binInt // 2
            # Else, increment
            else:
                binInt += 1
            # Increment output
            out += 1
        # Return output
        return out