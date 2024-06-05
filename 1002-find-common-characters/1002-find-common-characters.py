class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Make a counter of first word
        common = Counter(words[0])
        # Iterate through remaining words,
        for i in range(1, len(words)):
            # Make a counter of current word, update all first counter keys with min values
            curr = Counter(words[i])
            for k in common.keys():
                if k in curr:
                    common[k] = min(common[k], curr[k])
                else:
                    common[k] = 0
        # Keep an output array
        out = []
        # For each key in counter, append to output for each value
        for k, v in common.items():
            for x in range(v):
                out.append(k)
        # Return output
        return out