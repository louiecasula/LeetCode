# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edgecase: root is null
        if not root:
            return []
        # Keep a list of right node vals
        out = []
        # Use BFS to find right-most node vals
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            out.append(queue[-1].val)
            for i in range(n):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        # Return output list
        return out