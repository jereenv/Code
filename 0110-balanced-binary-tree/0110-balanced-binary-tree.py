# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True, 0
            
            is_lB, h1 = dfs(node.left)
            is_rB, h2 = dfs(node.right)
            
            is_B = abs(h1 - h2) <= 1
            
            h = max(h1, h2) + 1
            
            return is_B and is_lB and is_rB, h
        return dfs(root)[0]
            
            
        