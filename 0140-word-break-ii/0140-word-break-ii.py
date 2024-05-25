class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Keep an output array
        out = []
        # Function that checks all possible partitions of s
        def partition(substring, array):
            nonlocal out
            # Base case: substring matches s
            if substring == s and array not in out:
                out.append(" ".join(array))
            # Recursive case: check for words that equal the substring of s through word's length
            for word in wordDict:
                if word == s[len(substring): len(substring) + len(word)]:
                    partition(substring + word, array + [word])
        # Run function and return output
        partition("", [])
        return out