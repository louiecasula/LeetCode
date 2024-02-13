class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Iterate through words
        for word in words:
            # If element is the same backwards, return true
            if word == word[::-1]:
                return word
        return ""