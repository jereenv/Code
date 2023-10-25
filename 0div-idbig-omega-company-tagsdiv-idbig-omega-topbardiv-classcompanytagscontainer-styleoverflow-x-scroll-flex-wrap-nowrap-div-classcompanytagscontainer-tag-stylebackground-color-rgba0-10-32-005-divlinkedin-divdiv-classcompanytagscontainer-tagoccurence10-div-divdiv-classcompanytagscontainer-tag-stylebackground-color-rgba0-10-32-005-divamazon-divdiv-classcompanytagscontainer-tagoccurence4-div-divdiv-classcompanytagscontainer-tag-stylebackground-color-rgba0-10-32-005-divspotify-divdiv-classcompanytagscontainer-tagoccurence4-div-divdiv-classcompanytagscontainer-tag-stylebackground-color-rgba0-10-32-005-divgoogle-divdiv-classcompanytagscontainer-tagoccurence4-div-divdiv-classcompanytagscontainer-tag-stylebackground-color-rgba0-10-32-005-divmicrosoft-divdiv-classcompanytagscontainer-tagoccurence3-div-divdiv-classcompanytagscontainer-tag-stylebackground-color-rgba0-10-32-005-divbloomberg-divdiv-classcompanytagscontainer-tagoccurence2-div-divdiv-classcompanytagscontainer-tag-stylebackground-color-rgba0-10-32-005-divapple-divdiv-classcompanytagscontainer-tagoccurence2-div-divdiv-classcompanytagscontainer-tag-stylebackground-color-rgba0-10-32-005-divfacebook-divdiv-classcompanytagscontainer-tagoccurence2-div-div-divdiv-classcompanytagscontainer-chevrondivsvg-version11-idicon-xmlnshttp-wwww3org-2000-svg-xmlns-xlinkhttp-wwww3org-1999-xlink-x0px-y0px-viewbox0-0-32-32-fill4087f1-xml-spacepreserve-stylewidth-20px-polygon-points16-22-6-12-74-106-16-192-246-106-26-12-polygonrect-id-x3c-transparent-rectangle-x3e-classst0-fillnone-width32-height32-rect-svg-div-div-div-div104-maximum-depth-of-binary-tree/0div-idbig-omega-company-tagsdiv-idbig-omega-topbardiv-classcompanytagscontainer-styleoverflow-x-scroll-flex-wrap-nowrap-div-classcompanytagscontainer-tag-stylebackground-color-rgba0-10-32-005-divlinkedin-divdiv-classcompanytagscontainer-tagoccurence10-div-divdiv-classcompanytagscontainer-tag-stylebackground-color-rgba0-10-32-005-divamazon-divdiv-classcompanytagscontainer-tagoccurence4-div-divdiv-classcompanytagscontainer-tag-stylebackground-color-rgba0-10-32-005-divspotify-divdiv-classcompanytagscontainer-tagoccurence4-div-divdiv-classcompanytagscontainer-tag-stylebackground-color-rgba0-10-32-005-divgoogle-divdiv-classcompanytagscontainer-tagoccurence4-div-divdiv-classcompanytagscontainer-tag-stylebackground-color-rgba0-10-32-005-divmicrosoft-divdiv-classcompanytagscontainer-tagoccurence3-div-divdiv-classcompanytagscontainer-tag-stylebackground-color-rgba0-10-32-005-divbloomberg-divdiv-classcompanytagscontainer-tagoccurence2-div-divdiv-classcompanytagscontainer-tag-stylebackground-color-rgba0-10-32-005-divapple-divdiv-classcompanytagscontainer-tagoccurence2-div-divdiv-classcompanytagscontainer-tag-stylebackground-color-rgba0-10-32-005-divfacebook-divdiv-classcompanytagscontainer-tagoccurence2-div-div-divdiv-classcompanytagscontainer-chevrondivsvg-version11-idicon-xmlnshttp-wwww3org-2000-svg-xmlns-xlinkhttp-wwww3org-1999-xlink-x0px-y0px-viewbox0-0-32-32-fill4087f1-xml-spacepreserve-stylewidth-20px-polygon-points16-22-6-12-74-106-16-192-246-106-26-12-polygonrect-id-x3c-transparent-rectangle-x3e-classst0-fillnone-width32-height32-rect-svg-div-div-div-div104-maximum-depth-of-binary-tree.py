# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:

        if not node:
            return 0
        q = deque([node])
        level = 0
        while q:
            
            for i in range(len(q)):
                n = q.popleft()
                
                if n.left:
                    q.append(n.left)
                
                if n.right:
                    q.append(n.right)
            level += 1
        
        return level
            
            
            
            
            
            
