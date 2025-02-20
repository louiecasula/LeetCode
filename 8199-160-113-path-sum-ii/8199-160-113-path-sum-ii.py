# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Keep an output list
        out = []
        # DFS function to find all rtl paths with sums equal to targetSum
        def DFS(node, rSum, path):
            nonlocal out
            rSum += node.val
            if not node.left and not node.right and rSum == targetSum:
                out.append(path)
            if node.left:
                DFS(node.left, rSum, path + [node.left.val])
            if node.right:
                DFS(node.right, rSum, path + [node.right.val])
        # Run DFS function if root isn't null and return output
        if root:
            DFS(root, 0, [root.val])
        return out