class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Edgecase: strings are equal
        if str1 == str2:
            return str1
        # Keep an output string and variables for the min and max lengths
        out = ""
        Mlength = max(len(str1), len(str2))
        mlength = min(len(str1), len(str2))
        # Iterate until half the length of the longer string
        for i in range(Mlength // 2):
            # If length is divisible by i + 1 and slice is in shorter string, update output
            if Mlength % (i + 1) == 0 and mlength % (i + 1) == 0 and str1[:i + 1] * (len(str1) // (i + 1)) == str1 and str2[:i + 1] * (len(str2) // (i + 1)) == str2 and str1[:i + 1] == str2[:i + 1]:
                out = str1[:i + 1]
        # Return output
        return out