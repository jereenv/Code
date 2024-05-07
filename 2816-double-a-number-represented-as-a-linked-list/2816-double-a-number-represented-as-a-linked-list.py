# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(node):
            if not node:
                return 0
            
            node.val = 2 * node.val + dfs(node.next)
            
            if node.val > 9:
                node.val -= 10
                return 1
            
            return 0
        
        if dfs(head):
            return ListNode(val = 1, next = head)
        
        return head
        