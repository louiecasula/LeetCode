class Solution:
    def reverse(self, x: int) -> int:
        # If number is negative, remove sign
        neg = False
        if x < 0:
            neg = True
            x *= -1
        # Turn number into string, reverse it, back to int
        x = int(str(x)[::-1])
        # If it was negative, replace sign
        if neg:
            x *= -1
        # If x is outside of 32-bit int range, return 0. Else, return x
        if -2 ** 31 <= x and x <= 2 ** 31:
            return x
        return 0