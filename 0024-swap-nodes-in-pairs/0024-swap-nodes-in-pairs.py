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
        
        while curr and next:
            
            temp = next.next
            curr.next = temp
            next.next = curr
            prev.next = next
            
            prev = curr
            curr = curr.next
            if not curr or not curr.next:
                break
            next = curr.next
        
        return newH.next
            