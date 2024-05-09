class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Keep an output counter
        out = 0
        # Sort happiness in descending order
        happiness.sort(reverse=True)
        # Iterate to k, add the first value - i to output
        for i in range(k):
            out += max(0, happiness[i] - i)
        # Return output
        return out