class Solution:
    def reverseWords(self, s: str) -> str:
        # Keep an output string
        out = ""
        # Split string
        s = s.split(" ")
        # Pop each word and add to output string
        while s:
            word = s.pop()
            if len(word) > 0:
                out = out + word + " "
        return out.rstrip()