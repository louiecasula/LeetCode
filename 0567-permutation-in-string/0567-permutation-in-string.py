class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edgecase: s2 is smaller than s1
        if len(s1) > len(s2):
            return False
        # Map chars in s1 to their frequency
        sCount = defaultdict(int)
        for c in s1:
            sCount[c] += 1
        # Keep a l pointer and a map for the window
        l = 0
        wCount = defaultdict(int)
        # Iterate s2,
        for r, c in enumerate(s2):
            # Update map of window
            wCount[c] += 1
            if r - l > len(s1) - 1:
                wCount[s2[l]] -= 1
                if wCount[s2[l]] == 0:
                    del wCount[s2[l]]
                l += 1
            # If window map == s1 map, return true
            if sCount == wCount:
                return True
        # Return false if window reaches end
        return False