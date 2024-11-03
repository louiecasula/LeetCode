class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # If first char of first word != last char of last word, return false
        sentence = sentence.split(" ")
        if sentence[0][0] != sentence[-1][-1]:
            return False
        # Keep track of previous word
        prev = sentence[0]
        # Iterate sentence,
        for i in range(1, len(sentence)):
            # If last char of prev != first char of curr, return false
            curr = sentence[i]
            if prev[-1] != curr[0]:
                return False
            prev = curr
        # Return true
        return True