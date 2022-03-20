# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]):
        return self.dfs(root, 0)
    
    def dfs(self, root: Optional[TreeNode], path) -> int:
        if root is None:
            return 0
        
        path = 10 * path + root.val
        
        if root.left is None and root.right is None:
            return path
        
        return self.dfs(root.left, path) + self.dfs(root.right, path)
        
        