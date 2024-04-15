class Solution:
    def sumNumbers(self, root: TreeNode):
        ans = [0]
        
        
        def dp(node, curr):
            if node:
                curr = 10 * curr + node.val
                
                if not node.left and not node.right:
                    ans[0] += curr
                    return
                dp(node.left, curr)
                dp(node.right, curr)
            

        
        dp(root, 0)
        
        return ans[0]
            
        