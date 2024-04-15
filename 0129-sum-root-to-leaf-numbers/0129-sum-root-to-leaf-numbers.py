class Solution:
    def sumNumbers(self, root: TreeNode):
        
        def dp(node, curr):
            if not node:
                return 0
            
            curr = 10 * curr + node.val
            left = dp(node.left, curr)
            right = dp(node.right, curr)
            
            if not left and not right:
                return curr
            
        
            
            return left + right
    
        return dp(root, 0)
            
        