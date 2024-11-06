class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Convert each num into binary
        binStrings = ["{0:b}".format(x) for x in nums]
        # Convert each binString into its sum of set bits
        setBits = [x.count("1") for x in binStrings]
        # Keep a list of sequence of same set bits in nums
        seq = [[nums[0]]]
        # Iterate nums,
        for i in range(len(nums) - 1):
            # If current setBit is the same as the next, add num to current subsequence
            if setBits[i] == setBits[i + 1]:
                seq[-1].append(nums[i + 1])
            # Else, append a new subsequence to seq
            else:
                seq.append([nums[i + 1]])
        # Iterate seq,
        for i in range(len(seq) - 1):
            # If current subsequence's max isn't smaller than next subsequence's min, return False
            if max(seq[i]) > min(seq[i + 1]):
                return False
        return True