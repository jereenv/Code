# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node, tree):
        if not node:
            return True

        if not tree or node.val != tree.val:
            return False

        return (self.dfs(node.next, tree.left) or self.dfs(node.next, tree.right))
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if self.dfs(head, root):
            return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right) 