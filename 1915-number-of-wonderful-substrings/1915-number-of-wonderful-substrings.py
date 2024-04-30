class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Keep an output counter, a bitmask, and a hash table
        out = 0
        mask = 0
        count = defaultdict(int)
        count[0] = 1
        # Iterate through chars in word
        for c in word:
            # Get a 'a' == 0 mapped index of each char
            index = ord(c) - ord('a')
            # Use XOR by the left-shifted value of index to determine even/odd status
            mask ^= (1 << index)
            print(index, mask)
            # Add the number of even occurrence wonderful strings to output
            out += count[mask]
            # Iterate from 'a' -> 'j', checking the table for substrings before char's index
            for i in range(10):
                # Use an intermediate mask to determine previous char's even/odd status
                pre = mask ^ (1 << i)
                # Increment output by number of odd occurrence wonderful strings
                out += count[pre]
            # Increment current mask's count
            count[mask] += 1
        # Return output
        return out