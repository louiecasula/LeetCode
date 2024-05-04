# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Keep a list of good nodes
        good = 0
        # DFS function to find good nodes
        def DFS(node, path):
            nonlocal good
            if node.val >= max(path):
                good += 1
            if node.left:
                DFS(node.left, path + [node.left.val])
            if node.right:
                DFS(node.right, path + [node.right.val])
        # Run DFS function and return length of good node list
        DFS(root, [root.val])
        return good