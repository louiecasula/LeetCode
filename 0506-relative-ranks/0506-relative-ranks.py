class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Make a copy of score and sort scores in ascending order
        asc = sorted(score, reverse=True)
        # Iterate ascending scores,
        for i in range(len(asc)):
            # Set first through third as medal ranking strings, the rest are i + 1
            curr = score.index(asc[i])
            if i == 0:
                score[curr] = "Gold Medal"
            elif i == 1:
                score[curr] = "Silver Medal"
            elif i == 2:
                score[curr] = "Bronze Medal"
            else:
                score[curr] = str(i + 1)
        # Return score
        return score