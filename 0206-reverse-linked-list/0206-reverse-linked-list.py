# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev = head
            next = prev.next
            prev.next = None
            while next:
                temp = next.next
                next.next = prev
                prev = next
                next = temp
        
            head = prev
        return head
        