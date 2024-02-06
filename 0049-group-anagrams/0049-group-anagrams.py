class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create output list
        output = []
        # Create a map: key = sorted element, value = list of indexes
        dic = {}
        # Iterate through input
        for i in range(len(strs)):
            # If sorted element not in map,
            sort = ''.join(sorted(strs[i]))
            if sort not in dic:
                # Add sorted element and a list with the index
                dic[sort] = [i]
            # Else,
            else:
                # Append index to list of sorted element
                dic[sort].append(i)
        # Iterate through map values
        for i_list in dic.values():
            # Iterate through list
            for i in range(len(i_list)):
                # Change each index to it's element
                i_list[i] = strs[i_list[i]]
            # Append list to output
            output.append(i_list)
        # Return output
        return output