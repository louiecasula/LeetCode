class Solution:
    def removeStars(self, s: str) -> str:
        # Keep an output stack
        out = []
        # Iterate s,
        for char in s:
            # If current char is a star, pop output
            if char == "*":
                out.pop()
            # Else, add char to output
            else:
                out.append(char)
        # Return output
        return "".join(out)