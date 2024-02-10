class Solution:
    def countSubstrings(self, s: str) -> int:
        # Keep count variable
        count = 0
        # Keep string as list
        s = list(s)
        # Iterate through list (i)
        for i in range(len(s)):
            # Iterate through list (j = i)
            for j in range(i, len(s)):
                # If substring i:j + 1 == reverse,
                # print(s[i:j + 1], list(reversed(s[i:j + 1])))
                if s[i:j + 1] == list(reversed(s[i:j + 1])):
                    # Increment count
                    count += 1
        # Return count
        return count