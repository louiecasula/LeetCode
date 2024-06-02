class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Set a left pointer to 0 and a right pointer to final char
        l, r = 0, len(s) - 1
        # Iterate s while l is less than r,
        while l < r:
            # Save l char to temp variable, change l to r, r to temp
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            # Update both pointers
            l += 1
            r -= 1