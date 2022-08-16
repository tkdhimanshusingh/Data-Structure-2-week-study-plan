class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], left: int, right: int) -> bool:
            return not root or root.val > left and root.val < right and dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        
        return dfs(root, -math.inf, math.inf)