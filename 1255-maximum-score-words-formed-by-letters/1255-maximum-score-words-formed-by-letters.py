class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        # Map letter frequency and keep an output variable
        lettersCounter = Counter(letters)
        out = 0
        # Function that checks all valid word subsets and updates max score
        def explore(index, letterCounter, currScore):
            nonlocal out
            # Update output if a new max is reached
            out = max(out, currScore)
            # Base case: all subsets have been run
            if index == len(words):
                return
            # Recursive case: check all subsets
            for i in range(index, len(words)):
                # Deep copy counter and keep a variable for word's score and a validation flag
                tempCounter = copy.deepcopy(letterCounter)
                word = words[i]
                wordScore = 0
                isValid = True
                # Update letter frequency and word score for each letter in word
                for ch in word:
                    if ch in tempCounter and tempCounter[ch] > 0:
                        tempCounter[ch] -= 1
                        wordScore += score[ord(ch) - ord("a")]
                    else:
                        isValid = False
                        break
                # If word is able to be used, run function again on next word
                if isValid:
                    explore(i + 1, tempCounter, currScore + wordScore)
        # Run function and return output
        explore(0, lettersCounter, 0)
        return out