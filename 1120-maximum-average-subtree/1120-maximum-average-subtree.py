# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        ans = 0
        def dfs(node):
            if not node:
                return 0,0
            
            s_left, n_left = dfs(node.left)
            s_right, n_right = dfs(node.right)
            
            t_nodes = n_left + n_right + 1
            t_sum = s_left + s_right + node.val
            t_avg = t_sum/ t_nodes
            
            nonlocal ans
            ans = max(ans, t_avg)
            
            return t_sum, t_nodes
        
        
        dfs(root)
        return ans