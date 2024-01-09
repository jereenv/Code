# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        
        def dp(node, s):
            if node:
                if not node.left and not node.right:
                    if s == "1":
                        l1.append(node.val)
                    else:
                        l2.append(node.val)
                dp(node.left, s)
                dp(node.right, s)
        
        dp(root1, "1")
        dp(root2, "2")
        
        if l1 == l2:
            return True
        return False
                    
        