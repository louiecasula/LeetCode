class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Keep two pointers, sp and tp
        sp, tp = 0, 0
        N, M = len(s), len(t)
        # While both pointers are in bounds for their words,
        while sp < N and tp < M:
            # If s's current char is equal to t's char at tp, increment tp
            if s[sp] == t[tp]:
                tp += 1
            # Increment sp
            sp += 1
        # Return length of t - tp
        return M - tp