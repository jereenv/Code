# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node1 = p.val
        node2 = q.val
        
        def dfs(node):
            if node.val == node1:
                return p
            if node.val == node2:
                return q
          
            if node.val > node1 and node.val > node2:
                return dfs(node.left)
            
            if node.val < node1 and node.val < node2:
                return dfs(node.right)
            
            return node
            
            
        
        return dfs(root)
        