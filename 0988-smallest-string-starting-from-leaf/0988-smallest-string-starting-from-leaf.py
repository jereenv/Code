# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        res = ["z"*85000]
        
        def dfs(curr, node):
            if not node:
                res[0] = min(curr, res[0])
                return
            
            if not node.left and node.right:
                dfs(chr(node.val + 97) + curr, node.right)
            elif not node.right and node.left:
                dfs(chr(node.val + 97) + curr, node.left)
            else:
                dfs(chr(node.val + 97) + curr, node.right)
                dfs(chr(node.val + 97) + curr, node.left)
                
            

        dfs("", root)
        return res[0]