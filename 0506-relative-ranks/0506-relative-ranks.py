class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Keep an output list and save length in variable
        n = len(score)
        out = [""] * n
        # Map each score to its index
        score_map = defaultdict(int)
        for i in range(n):
            score_map[score[i]] = i
        # Sort scores in ascending order
        score.sort(reverse=True)
        # Iterate ascending scores,
        for i in range(n):
            # Set first through third as medal ranking strings, the rest are i + 1
            if i == 0:
                out[score_map[score[i]]] = "Gold Medal"
            elif i == 1:
                out[score_map[score[i]]] = "Silver Medal"
            elif i == 2:
                out[score_map[score[i]]] = "Bronze Medal"
            else:
                out[score_map[score[i]]] = str(i + 1)
        # Return score
        return out