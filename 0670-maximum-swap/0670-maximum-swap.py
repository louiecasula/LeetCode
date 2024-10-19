class Solution:
    def maximumSwap(self, num: int) -> int:
        # Make num a list of digits
        numList = [int(x) for x in str(num)]
        # Iterate num,
        for i in range(len(numList) - 1):
            # If max of right digits <= ith digit, continue
            rMax = max(numList[i + 1:])
            if rMax <= numList[i]:
                continue
            # Iterate backwards to i,
            for j in range(len(numList) - 1, i - 1, -1):
                # If j == max of right, swap chars and return joined int of numList
                if numList[j] == rMax:
                    numList[j], numList[i] = numList[i], numList[j]
                    return int("".join([str(x) for x in numList]))
        # Return num
        return num