class Solution:
    def decodeString(self, s: str) -> str:
        # Keep an output stack
        out = []
        # Iterate s,
        for char in s:
            # If curr char isn't a closing bracket, append to stack
            if char != "]":
                out.append(char)
            # Else,
            else:
                # Keep an empty string, ss
                ss = ""
                # While top of stack isn't an opening bracket, add popped char to beginning of ss
                while out[-1] != "[":
                    ss = out.pop() + ss
                # Pop the opening bracket
                out.pop()
                # Keep another empty string, numStr
                numStr = ""
                # While top of stack is a digit, add popped digit to beginning of numStr
                while out and out[-1].isdigit():
                    numStr = out.pop() + numStr
                # Add numStr * ss to stack
                out.append(int(numStr) * ss)
        # Return output as joined string
        return "".join(out)