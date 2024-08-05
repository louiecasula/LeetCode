class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Map frequency of elements in in arr
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1
        # Make a list of all elements with only one appearance
        dist = [x[0] for x in freq.items() if x[1] == 1]
        # Return kth element if possible, else empty string
        return dist[k - 1] if len(dist) >= k else ""