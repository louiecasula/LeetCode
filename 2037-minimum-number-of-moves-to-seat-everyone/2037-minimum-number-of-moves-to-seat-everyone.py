class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort both arrays
        seats.sort()
        students.sort()
        # Keep an output variable
        out = 0
        # Iterate arrays, add absolute difference between ith value to output
        for i in range(len(seats)):
            out += abs(seats[i] - students[i])
        # Return output
        return out