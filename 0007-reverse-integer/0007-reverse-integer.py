class Solution:
    def reverse(self, x: int) -> int:
        # If number is negative, remove sign
        neg = False
        if x < 0:
            neg = True
            x *= -1
        # Turn number into string, reverse it
        x = list(reversed(list(str(x))))
        # If it was negative, replace sign
        if neg:
            x.insert(0, "-")
        # Convert back to number
        x = int(''.join(x))
        # If x is outside of 32-bit int range, return 0. Else, return x
        if -2147483648 <= x and x <= 2147483647:
            return x
        return 0