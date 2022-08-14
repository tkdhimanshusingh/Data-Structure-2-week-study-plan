# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global s,flag
        s=0
        flag=0
        def solver(r):
            if not r:
                return
            global s
            global flag
            s+=r.val
            if s==targetSum and not (r.left or r.right):
                print("Hi")
                flag=1
                return
            if r.left:
                solver(r.left)
                s-=r.left.val
            if r.right:
                solver(r.right)
                s-=r.right.val
        solver(root)
        if flag==1:
            return True
        else:
            return False