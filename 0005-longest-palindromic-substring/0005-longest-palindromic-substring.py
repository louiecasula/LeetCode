class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Keep an output string
        out = ""
        # Iterate string, checking that i - 1 == i + 1, and updating output
        for i in range(len(s)):
            j = 0
            while i - j >= 0 and i + j < len(s):
                # print(s[i - j: i + j + 1])
                if s[i - j] != s[i + j]:
                    break
                if len(s[i - j: i + j + 1]) > len(out):
                    out = s[i - j: i + j + 1]
                j += 1
            j = 0
            if i + 1 < len(s) and s[i] == s[i + 1]:
                while i - j >= 0 and i + 1 + j < len(s):
                    # print(s[i - j: i + j + 2])
                    if s[i - j] != s[i + 1 + j]:
                        break
                    if len(s[i - j: i + j + 2]) > len(out):
                        out = s[i - j: i + j + 2]
                    j += 1
        # Return output
        return out