class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Sort strs by length
        asc = sorted(strs, key=len)
        # Use smallest word as target
        tar = asc[0]
        # Iterate backwards by target length
        for i in range(len(tar), -1, -1):
            common = True
            # If all remaining words begin with target substring,
            for str in strs:
                if str[:i] != tar[:i]:
                    common = False
                    break
            if common:
                # Return substring
                return tar[:i]