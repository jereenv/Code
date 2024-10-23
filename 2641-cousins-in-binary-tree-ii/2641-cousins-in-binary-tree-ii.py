# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = [[root, 0]]
        
        
        while q:
            level = []
            
            for node, _ in q:
                if node.left:
                    level.append([node.left, node.right.val if node.right else 0] )
                if node.right:
                    level.append([node.right, node.left.val if node.left else 0])
        
            s = sum([x.val for x, _ in level])
                        
            for node, cuz in level:
                node.val = s - node.val - cuz
            
            q = level
        root.val = 0
        return root
                
        