class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        # Sort coins
        coins = sorted(coins)
        # Keep an output variable and a max sum variable
        out = reachable = 0
        # Iterate coins,
        for coin in coins:
            # While reachable is less than current coin - 1,
            while reachable < coin - 1:
                # Double reachable and add 1
                reachable = 2 * reachable + 1
                # Increment output
                out += 1
            # Add current coin to reachable
            reachable += coin
        # While reachable is less than target,
        while reachable < target:
            # Double reachable and add 1
            reachable = 2 * reachable + 1
            # Increment output
            out += 1
        # Return out
        return out