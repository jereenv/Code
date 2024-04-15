class Solution:
    def sumNumbers(self, root: TreeNode):
        
        def dp(node, curr):
            if not node:
                return 0
            
            curr = 10 * curr + node.val
            
            if not node.left and not node.right:
                return curr
            
            return dp(node.left, curr) + dp(node.right, curr)
    
        return dp(root, 0)
            
        