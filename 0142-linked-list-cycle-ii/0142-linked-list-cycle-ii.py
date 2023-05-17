# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        h = head
        while h and h.next:
            t = t.next
            h = h.next.next
            if t == h:
                break
        else:
            return
        t = head
        while t != h:
            t = t.next
            h = h.next
        return t
        
        