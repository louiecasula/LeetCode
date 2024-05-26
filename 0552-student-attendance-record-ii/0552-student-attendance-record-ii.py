class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        cache = {}
        def count(n):
            if n == 1:
                return {
                    (0, 0): 1, (0, 1): 1, (0, 2): 0,
                    (1, 0): 1, (1, 1): 0, (1, 2): 0,
                }
            if n in cache:
                return cache[n]
            temp = count(n - 1)
            out = defaultdict(int)

            # P
            out[(0, 0)] = ((temp[(0, 0)] + temp[(0, 1)]) % MOD + temp[(0, 2)]) % MOD
            out[(1, 0)] = ((temp[(1, 0)] + temp[(1, 1)]) % MOD + temp[(1, 2)]) % MOD

            # L
            out[(0, 1)] = temp[(0, 0)]
            out[(1, 1)] = temp[(1, 0)]
            out[(0, 2)] = temp[(0, 1)]
            out[(1, 2)] = temp[(1, 1)]

            # A
            out[(1, 0)] = (out[(1, 0)] + (((temp[(0, 0)] + temp[(0, 1)]) % MOD + temp[(0, 2)])) % MOD) % MOD
            cache[n] = out
            return out
        return sum(count(n).values()) % MOD