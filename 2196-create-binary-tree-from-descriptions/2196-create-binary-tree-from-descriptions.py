# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Keep a dict for nodes with parents as values
        parentMap = dict()
        children = set()
        p = c = None
        # Iterate through descriptions,
        for d in descriptions:
            # Update children set
            children.add(d[1])
            # If parent or child isn't in dict, make a node for it,
            if d[1] not in parentMap:
                c = TreeNode(val=d[1])
                parentMap[d[1]] = c
            else:
                c = parentMap[d[1]]
            if d[0] not in parentMap:
                p = TreeNode(val=d[0])
                parentMap[d[0]] = p
            else:
                p = parentMap[d[0]]
            # If isLeft is 1 make child left of parent, else right
            if d[2] == 1:
                p.left = c
            else:
                p.right = c
        # Iterate descriptions,
        for d in descriptions:
            # If parent not in children, return parent
            if d[0] not in children:
                return parentMap[d[0]]