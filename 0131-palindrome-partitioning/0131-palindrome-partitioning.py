class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Keep an output array
        out = []
        N = len(s)
        # Function to find palindrome up to current index
        def palindrome(index, stringArr):
            nonlocal out
            if index == N:
                out.append(stringArr)
                return
            for i in range(index, N):
                if s[index:i + 1] == s[index:i + 1][::-1]:
                    palindrome(i + 1, stringArr + [s[index:i + 1]])
        # Run function and return output
        palindrome(0, [])
        return out