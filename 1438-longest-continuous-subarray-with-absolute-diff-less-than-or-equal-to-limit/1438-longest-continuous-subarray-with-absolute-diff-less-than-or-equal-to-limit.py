class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Keep a max and min deque, l pointer, and output variable
        max_deque = deque()
        min_deque = deque()
        l = 0
        out = 0
        # Iterate nums,
        for r in range(len(nums)):
            # Maintain max_deque and min_deque
            while max_deque and nums[r] > max_deque[-1]:
                max_deque.pop()
            while min_deque and nums[r] < min_deque[-1]:
                min_deque.pop()
            max_deque.append(nums[r])
            min_deque.append(nums[r])
            # Check if current window is valid
            while max_deque[0] - min_deque[0] > limit:
                if nums[l] == max_deque[0]:
                    max_deque.popleft()
                if nums[l] == min_deque[0]:
                    min_deque.popleft()
                l += 1
            # Update output with current window size
            out = max(out, r - l + 1)
        # Return out
        return out