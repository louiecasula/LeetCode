# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Keep an output list
        out = [0]
        # BFS traversal function that keeps track of level
        def bfs(root, lvl):
            if not root:
                return
            if lvl < len(out):
                out[lvl] += root.val
            else:
                out.append(root.val)
            bfs(root.left, lvl + 1)
            bfs(root.right, lvl + 1)
        # Run BFS function and return kth element of sorted output
        bfs(root, 0)
        return sorted(out, reverse=True)[k - 1] if k <= len(out) else -1