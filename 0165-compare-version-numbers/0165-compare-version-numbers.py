class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split both versions by "."
        v1 = deque(version1.split("."))
        v2 = deque(version2.split("."))
        # Shift each num in v1 and v2,
        while v1 or v2:
            s1 = int(v1.popleft()) if len(v1) > 0 else 0
            s2 = int(v2.popleft()) if len(v2) > 0 else 0
            # If v1 > v2, return 1. If v2 > v1, return -1
            if s1 > s2:
                return 1
            if s2 > s1:
                return -1
        # Return 0
        return 0