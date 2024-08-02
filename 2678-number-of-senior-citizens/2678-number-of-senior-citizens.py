class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Keep an output counter
        out = 0
        # Iterate details,
        for d in details:
            # If the 11th char is at least "6" and the 12th is at least "1", increment counter
            if int(d[11:13]) > 60:
                out += 1
        # Return output
        return out