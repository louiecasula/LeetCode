class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Map frequency of elements in in arr
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1
        # Return kth key whose val is 1, else empty string
        for key in freq.keys():
            if freq[key] == 1:
                k -= 1
            if k == 0:
                return key
        return ""