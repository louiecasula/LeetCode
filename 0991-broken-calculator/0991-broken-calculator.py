class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # Keep an output variable
        out = 0
        # While target is greater than startValue,
        while target > startValue:
            # If target is even, half it
            if target % 2 == 0:
                target /= 2
            # Else, add 1
            else:
                target += 1
            # Increment output
            out += 1
        # Return output and the difference between new target value and startValue
        # This saves the time of repeatedly adding 1 if target is less than startValue
        return out + int(startValue - target)