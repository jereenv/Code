# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(right, left):
            if not right and not left:
                return True
            
            if not right or not left:
                return False
            
            if right.val != left.val:
                return False
            
            return check(right.right, left.left) and check(right.left, left.right)
        
        return check(root.right, root.left)
            
                
        