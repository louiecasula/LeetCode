class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Edgecase: There aren't enough flowers
        if len(bloomDay) < m * k:
            return -1
        # Helper function to check if m bouqets are possible in a given range
        def canMakeBouquets(bloomDay, m, k, day):
            total = 0
            flowers = 0
            for b in bloomDay:
                if b <= day:
                    flowers += 1
                    if flowers == k:
                        total += 1
                        flowers = 0
                else:
                    flowers = 0
                if total >= m:
                    return True
            return False
        # Keep a low and high variable
        low, high = 1, max(bloomDay)
        # Use binary search, adjusting low and high depending on helper function result
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(bloomDay, m, k, mid):
                high = mid
            else:
                low = mid + 1
        # Return lowest possible bloomDay val
        return low