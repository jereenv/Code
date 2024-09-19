# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        bfs = []
        
        if root:
            ans.append(root.val)
            bfs.append(root)

        while bfs:
            
            temp = []
            
            for node in bfs:
                if node.left:
                    temp.append(node.left)
                
                if node.right:
                    temp.append(node.right)
            
            bfs = temp
            if temp:
                ans.append(temp[-1].val)
        
        return ans
        