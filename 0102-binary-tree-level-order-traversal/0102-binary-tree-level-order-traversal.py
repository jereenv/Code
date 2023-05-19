# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        nodes = [root]
        
        def dfs(node):
            if node:
                #ans.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        if root:
            while nodes:
                level = []
                ans.append([i.val for i in nodes])
                for i in nodes:
                    dfs(i)
                nodes = level
        return ans