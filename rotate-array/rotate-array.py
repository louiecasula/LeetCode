class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If k is greater than or equal to length, subtract length from it until it is less than length
        k %= len(nums)
        # Iterate for k, pop each val and insert at beginning of list
        for i in range(k):
            x = nums.pop()
            nums.insert(0,x)
        return nums