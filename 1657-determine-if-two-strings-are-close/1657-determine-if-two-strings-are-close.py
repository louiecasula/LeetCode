class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Make a counter of both words
        c1, c2 = Counter(word1), Counter(word2)
        # If keys aren't the same, return false
        if sorted(list(c1.keys())) != sorted(list(c2.keys())):
            return False
        # If values aren't the same, return false
        return sorted(list(c1.values())) == sorted(list(c2.values()))