class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # While the sum of chalk is greater than k, decrement k by sum of chalk
        k %= sum(chalk)
        # Iterate through chalk,
        for i in range(len(chalk)):
            # If k < chalk[i], return i
            if k < chalk[i]:
                return i
            # Else, decrement k by chalk[i]
            k -= chalk[i]