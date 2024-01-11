class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def dfs(node, m1, m2):
            if not node:
                return m1 - m2
            
            m1 = max(m1, node.val)
            m2 = min(m2, node.val)
            
            mlt1 = dfs(node.left, m1, m2)
            mrt1 = dfs(node.right, m1, m2)
            
            return max(mlt1, mrt1)
        
        return dfs(root, -1, 10**5 + 1 )
            
            
            