# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ans = 0
    low = 0
    high = 0
    
    def dp(self, node):
        if not node:
            return

        if node.val >= self.low and node.val <= self.high:
            self.ans += node.val

        self.dp(node.left)
        self.dp(node.right)
            
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        
            
        self.dp(root)
        return self.ans
        