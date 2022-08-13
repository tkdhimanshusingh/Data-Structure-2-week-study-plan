# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solver(r):
            if r==None:
                return 0
            return 1+max(solver(r.left),solver(r.right))
        return solver(root)