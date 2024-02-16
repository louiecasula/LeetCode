class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Map frequencies of numbers
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        # Make a list with nums from smallest to largest freq
        sort_freq = dict(sorted(freq.items(), key=lambda item: item[1]))
        sort_list = []
        for key in sort_freq:
            for i in range(sort_freq[key]):
                sort_list.append(key)
        print(sort_list)
        # Delete first k amount of elements
        sort_list = sort_list[k:]
        print(sort_list)
        # Make a set from the list
        set_list = set(sort_list)
        print(set_list)
        # Return the size of the set
        return len(set_list)