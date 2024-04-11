class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Keep an output stack
        out = []
        # Iterate numstring,
        for d in num:
            # If k > 0, out isn't empty, and latest output el is greater than curr el,
            while k > 0 and out and out[-1] > d:
                # Decrement k and pop from output
                k -= 1
                out.pop()
            # Else, push curr el to output
            out.append(d)
        # If k is still > 0, remove from end of numstring
        out = out[:len(out) - k]
        # Join output stack
        out = "".join(out)
        # Strip leading zeroes
        out = out.lstrip("0")
        # Return output if not empty, else "0"
        return str(out) if out else "0"