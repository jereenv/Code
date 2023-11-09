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
            
            v1, left_h = dfs(node.left)
            v2, right_h = dfs(node.right)
            if not(v1 and v2):
                return False, 0
            
            isB = abs(left_h - right_h) <= 1
            
            return isB, 1 + max(left_h, right_h)
        
        return dfs(root)[0]
                
            
            
        