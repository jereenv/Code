# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        ans = [0]
        
        def checkPalin(dic):
            odd = 0
            for i in dic:
                if dic[i]%2 != 0:
                    odd += 1
                if odd > 1:
                    return False
            return True
        
        def dp(node, dic):
            dic[node.val] += 1
            if node.left:
                dp(node.left, dic.copy())
            if node.right:
                dp(node.right, dic.copy())
            if not node.left and not node.right:
                if checkPalin(dic):
                    ans[0] += 1
            
        dp(root, defaultdict(int))
        return ans[0]
        
        
         
            
            
                
        