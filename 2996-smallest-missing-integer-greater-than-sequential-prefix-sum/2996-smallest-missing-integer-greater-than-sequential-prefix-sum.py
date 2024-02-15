class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ## Find longest sequential prefix ##
        # Keep a list for the sequence
        seq = [nums[0]]
        # Iterate through nums
        for i in range(len(nums) - 1):
            # If nums[i + 1] == nums[i] + 1,
            if nums[i + 1] == nums[i] + 1:
                # Add to sequence list and continue
                seq.append(nums[i + 1])
                continue
            # Else, break loop
            break
        ## Find smallest missing int that's >= sum of sequence ##
        # Save the sum of the sequence
        tar = sum(seq)
        # Loop
        while True:
            # If the sum is not in list,
            if tar not in nums:
                # Return sum
                return tar
            # Else, increment sum
            tar += 1