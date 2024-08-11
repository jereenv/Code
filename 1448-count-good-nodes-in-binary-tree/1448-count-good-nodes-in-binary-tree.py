# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = [0]
        def dfs(node, m):
            if node:
                if node.val >= m:
                    m = node.val
                    ans[0] += 1
                
                dfs(node.left, m)
                dfs(node.right, m)
        
        dfs(root, -float('inf'))
        return ans[0]
            
        