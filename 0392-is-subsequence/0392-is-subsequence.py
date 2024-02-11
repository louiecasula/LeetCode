class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Handle edge cases
        if s == "":
            return True
        # Keep a count (i) and a comparison string
        i = 0
        mod = ""
        # Iterate through t (j)
        for j in range(len(t)):
            print(i, j)
            if s == mod:
                return True
            # If t[j] == s[i],
            if t[j] == s[i]:
                # Add to comparison string
                mod += t[j]
                i += 1
        # If s == t, return true
        print(s, mod)
        return s == mod