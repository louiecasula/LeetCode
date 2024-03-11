class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Make a pre string
        pre = ""
        freq = {}
        # Map frequency of chars in s
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        # For each char in order,
        for char in order:
            # If it's in freq, append all instances to pre
            if char in freq:
                pre += char * freq[char]
                s = s.replace(char, "")
        # Return pre + s
        return pre + s