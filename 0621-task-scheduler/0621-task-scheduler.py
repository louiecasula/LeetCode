class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Keep a count variable, and a sequence queue
        count = 0
        seq = []
        # List frequencies of tasks and sort in desc order
        types = list(set(tasks))
        freq = []
        for i in range(len(types)):
            freq.append(tasks.count(types[i]))
        freq = sorted(freq, reverse=True)
        # Populate queue with a list of frequencies and an incrementing 0-index
        for i in range(len(freq)):
            seq.append([freq[i], i])
        # While queue isn't empty,
        while len(seq) > 0:
            # If first element's index isn't equal to count, increment count and continue
            if seq[0][1] > count:
                count += 1
                continue
            # Pop left, decrement freq, increment index by n
            curr = seq.pop(0)
            curr[0] -= 1
            curr[1] += n + 1
            # If freq > 0, append
            if curr[0] > 0:
                seq.append(curr)
            count += 1
        # Return count
        return count