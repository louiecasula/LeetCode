class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # Keep an output counter
        out = 0
        # Iterate rating until -2 of rating,
        N = len(rating)
        for m in range(1, N - 1):
            # Keep lSmall and rLarge counters
            lSmall = rLarge = 0
            # Iterate from start to m, update lSmall
            for i in range(0, m):
                if rating[i] < rating[m]:
                    lSmall += 1
            # Iterate from m to end, update rLarge
            for i in range(m + 1, N):
                if rating[i] > rating[m]:
                    rLarge += 1
            # Increment output by product of lSmall & rLarge + product of m - lSmall & N - rLarge
            out += (lSmall * rLarge) + ((m - lSmall) * (N - m - 1 - rLarge))
        # Return output
        return out