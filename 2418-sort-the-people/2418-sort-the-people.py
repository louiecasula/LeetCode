class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Zip names and heights together, sort, return list comp of names
        nh = list(zip(heights, names))
        nh.sort(reverse=True)
        return [x[1] for x in nh]