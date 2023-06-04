# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next, slow = None, slow.next
        slow = self._reverseList(slow)

        while slow and head:
            head.next, head = slow, head.next
            slow.next, slow = head, slow.next
    
    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur, nex = None, head, head.next

        while nex:
            cur.next = pre
            pre = cur
            cur = nex
            nex = nex.next
        cur.next = pre
        return cur