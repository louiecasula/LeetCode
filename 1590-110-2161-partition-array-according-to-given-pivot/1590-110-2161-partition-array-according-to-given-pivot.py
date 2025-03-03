class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Keep a pre, inter, and post list
        pre, inter, post = [], [], []
        # Iterate nums,
        for num in nums:
            # If num < pivot, append to pre
            if num < pivot:
                pre.append(num)
            # Elif num == pivot, append to inter
            elif num == pivot:
                inter.append(num)
            # Else, append to post
            else:
                post.append(num)
        # Return pre + inter + post
        return pre + inter + post