# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        
        node1 = dummy
        node2 = head
        
        while n:
            node2 = node2.next
            n -= 1
        
        while node2:
            node2 = node2.next
            node1 = node1.next
            
        node1.next = node1.next.next
        
        return dummy.next
    
            
        