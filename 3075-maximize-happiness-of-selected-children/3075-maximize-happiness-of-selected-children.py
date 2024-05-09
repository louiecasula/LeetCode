class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Keep an output counter
        out = 0
        # Sort happiness in ascending order
        happiness.sort()
        # Iterate to k, add the popped value - i to output
        for i in range(k):
            curr = happiness.pop()
            out += max(0, curr - i)
        # Return output
        return out