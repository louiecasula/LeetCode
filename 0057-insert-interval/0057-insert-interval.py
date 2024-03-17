class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Make an output array
        out = []
        # Iterate intervals,
        for i in range(len(intervals)):
            # If newInt ends before currInt begins, add newInt to output followed by remaining intervals and return
            if newInterval[1] < intervals[i][0]:
                out.append(newInterval)
                return out + intervals[i:]
            # If newInt begins after currInt ends, append currInt to output
            if newInterval[0] > intervals[i][1]:
                out.append(intervals[i])
            # Else, merge newInt with currInt
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # Append newInterval to output and return
        out.append(newInterval)
        return out