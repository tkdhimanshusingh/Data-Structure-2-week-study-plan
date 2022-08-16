class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_table = {}
        return self.findTargetHelper(root, k, hash_table)
    
    
    def findTargetHelper(self, root, k, hash_table) -> bool:
        if root is None:
            return False
        
        complement = k - root.val
        
        if complement in hash_table:
            return True
        
        hash_table[root.val] = True
        
        return (
            self.findTargetHelper(root.left, k, hash_table) or
            self.findTargetHelper(root.right, k, hash_table))