class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Function to find nth binString
        def createBinString(m) -> str:
            # Base case: m is 1
            if m == 1:
                return "0"
            # Recursive case: Apply rules for Nth binString
            binString = createBinString(m - 1)
            temp = int(binString, 2)
            inverse = temp ^ (2 ** (len(binString) + 1) - 1)
            res = bin(inverse)[3 : ]
            return binString + "1" + res[::-1]
        # Return k - 1th char of binString
        return createBinString(n)[k - 1]