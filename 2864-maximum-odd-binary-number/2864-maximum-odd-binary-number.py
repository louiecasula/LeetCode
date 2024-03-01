class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = s.replace("1", "", 1)
        s = ''.join(sorted(s, reverse=True))
        return s + "1"