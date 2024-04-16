# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        dummy = TreeNode(left = root)
        
        curr = dummy
        
        temp = []
        
        q = [dummy]

        
        while depth > 1:
            
            for n in q:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            depth -= 1
            q = temp
            temp = []
        
        for n in q:
            if n.left:
                n.left = TreeNode(left = n.left, val = val)
            else:
                n.left = TreeNode(val = val)
            if n.right:
                n.right = TreeNode(right = n.right, val = val)
            else:
                n.right = TreeNode(val = val)
        return dummy.left
            
            