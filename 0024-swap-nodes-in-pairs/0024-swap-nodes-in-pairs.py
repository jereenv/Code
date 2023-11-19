# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        
        
        prev = ListNode(head)
        newH = prev
        curr = head
        next = head.next
        
        while curr and curr.next:
            
            next = curr.next
            
            prev.next = next
            curr.next = next.next
            next.next = curr
            
            
            prev = curr
            curr = curr.next

        
        return newH.next
            