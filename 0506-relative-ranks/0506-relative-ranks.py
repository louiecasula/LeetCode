class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Make a copy of score and sort scores
        desc = sorted(score)
        n = len(desc)
        # Iterate ascending scores,
        for i in range(len(desc)):
            # Set first through third as medal ranking strings, the rest are i + 1
            curr = score.index(desc[i])
            if i == n - 1:
                score[curr] = "Gold Medal"
            elif i == n - 2:
                score[curr] = "Silver Medal"
            elif i == n - 3:
                score[curr] = "Bronze Medal"
            else:
                score[curr] = str(n - i)
        # Return score
        return score