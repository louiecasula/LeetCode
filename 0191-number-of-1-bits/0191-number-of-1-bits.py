class Solution:
    def hammingWeight(self, n: int) -> int:
        # Keep a count
        count = 0
        m = int(str(bin(n)[2:]))
        # While n is greater than or 1,
        while m >= 1:
            # If mod 10 is 1, increment count
            if m % 10 == 1:
                count += 1
            # Divide by 10
            m = m // 10
        # Return count
        return count