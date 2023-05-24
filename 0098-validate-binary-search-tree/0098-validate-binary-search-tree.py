# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        












        
        m1 = -2**31 - 1
        m2 = 2**31 + 1
        
        def dfs(node, m1, m2):
            
            ans = True
            if node.val >= m2:
                return False
            if node.val <= m1:
                return False
            
            if node.left:
                ans = ans and dfs(node.left, m1, node.val)
            
            if node.right:
                ans = ans and dfs(node.right, node.val, m2)
            
            return ans
    
        return dfs(root, m1, m2)
                
                
            
        