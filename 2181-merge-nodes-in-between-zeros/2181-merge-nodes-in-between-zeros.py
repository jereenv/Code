# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        
        t, h = dummy, dummy.next.next
        
        curr = 0 
        
        while h:
            if h.val == 0:
                t = t.next
                t.val = curr
                curr = 0
            
            curr += h.val
            h = h.next
        
        t.next = None
        
        return dummy.next
                
        
        