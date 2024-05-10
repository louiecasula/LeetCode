class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Map all possible division pairs and their quotients
        fractions = defaultdict(list)
        for numer in arr:
            for denom in arr:
                if numer != denom and numer < denom:
                    fract = numer / denom
                    fractions[fract].extend([numer, denom])
        # Make a list from their quotients and sort in ascending order
        quotients = sorted(list(fractions.keys()))
        # Return kth value in map
        return fractions[quotients[k - 1]]