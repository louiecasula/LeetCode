# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Keep lists of lead nodes for both trees
        l1, l2 = [], []
        # DFS function to find all leaf nodes
        def DFS(node,leafs):
            if not node.left and not node.right:
                leafs.append(node.val)
            if node.left:
                DFS(node.left, leafs)
            if node.right:
                DFS(node.right, leafs)
        # Run DFS on both trees and return if their leaf node lists are the same
        DFS(root1, l1)
        DFS(root2, l2)
        return l1 == l2