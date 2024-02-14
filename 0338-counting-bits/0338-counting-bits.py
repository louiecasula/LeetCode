class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            oc = 0
            while i > 0:
                if i % 2 == 1:
                    oc += 1
                i = i // 2
            ans.append(oc)
        return ans