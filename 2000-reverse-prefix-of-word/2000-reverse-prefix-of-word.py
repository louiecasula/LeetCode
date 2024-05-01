class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find index of ch if it's in word
        if ch in word:
            # Return the modified word
            return ''.join(reversed(list(word[:word.index(ch) + 1]))) + word[word.index(ch) + 1:]
        # Else, just return the original word
        return word