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
        
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        secondH = slow.next
        slow.next = None
        prev = None
        
        while secondH:
            temp = secondH.next
            secondH.next = prev
            prev = secondH
            secondH = temp
            
        firstH = head
        secondH = prev
        
        while secondH:
            temp1 = firstH.next
            temp2 = secondH.next
            firstH.next = secondH
            secondH.next = temp1
            firstH = temp1
            secondH = temp2
        
        
        