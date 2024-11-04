class Solution:
    def compressedString(self, word: str) -> str:
        # Keep an output string, current char and a counter
        out = ""
        N = len(word)
        curr, counter = word[0], 1
        # Iterate word,
        for i in range(1, N):
            if word[i] == curr and counter < 9:
                counter += 1
            # Elif curr != current char, append counter and curr to output, update curr and reset counter
            else:
                out += str(counter) + curr
                curr, counter = word[i], 1
        # Return output string + counter + final char
        return out + str(counter) + curr
