# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(next = head)
        h = t = dummy
        curr = head
        
        while h.next:
            h = h.next.next
            
            prev = t
            t = curr
            curr = t.next
            t.next = prev

        h = curr
        ans = 0
        while h:
            ans = max(ans, h.val + t.val)
            h = h.next
            t = t.next
        return ans
        
        