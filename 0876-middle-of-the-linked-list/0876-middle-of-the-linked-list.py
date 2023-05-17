# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        h = head
        while h.next != None:
            h = h.next
            t = t.next
            if not h.next:
                break
            h = h.next
        return t
        