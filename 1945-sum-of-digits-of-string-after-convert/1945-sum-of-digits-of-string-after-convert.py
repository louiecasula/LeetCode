class Solution:
    # Function to add digits together
    def addDigits(self, num: int) -> int:
        newNum = 0
        while num > 0:
            dig = num % 10
            num //= 10
            newNum += dig
        return newNum

    def getLucky(self, s: str, k: int) -> int:
        # Convert s to a string of ints
        out = ""
        for c in s:
            out += str(ord(c) - 96)
        out = int(out)
        # Iterate to k,
        for i in range(k):
            # If output is less than 10, return it
            if out < 10:
                return out
            # Add all digits together
            out = self.addDigits(out)
        # Return output
        return out