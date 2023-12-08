# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        def dfs(node):
            
           
            if not node:
                return 0
            
            s_left = dfs(node.left)
            s_right = dfs(node.right)
            
            if node.val == s_left + s_right:
                nonlocal ans
                ans += 1
            
            return node.val + s_left + s_right
        
        dfs(root)
        return ans
        