# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Works for situation when there is a swap between parent and child
        '''
        def dfs(node, parents_L, parents_R):
            
            if node:
                for idx, parent in enumerate(parents_L):
                    if parent.val < node.val:
                        node.val, parent.val = parent.val, node.val
                        return
                for idx, parent in enumerate(parents_R):
                    if parent.val > node.val:
                        node.val, parent.val = parent.val, node.val
                        return
                
                dfs(node.left, parents_L + [node], parents_R)
                dfs(node.right, parents_L, parents_R + [node])
        
        dfs(root, [], [])
        '''
        
        def inorderTraversal(node):
            return inorderTraversal(node.left) + [node] + inorderTraversal(node.right) if node else []
        
        def find_swapped(tree_list):
            
            first, second = None, None
            
            for i in range(len(tree_list) - 1):
                if tree_list[i + 1].val < tree_list[i].val:
                    second = tree_list[i + 1]
                    if first is None:
                        first = tree_list[i]
                    else:
                        break
            return first, second
        
        
        first, second = find_swapped(inorderTraversal(root))
        
        first.val, second.val = second.val, first.val
        
        
                
            
            
                
                        
                        
                        
                        
                        
            