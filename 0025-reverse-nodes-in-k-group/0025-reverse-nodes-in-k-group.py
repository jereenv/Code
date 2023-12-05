# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        
        
        def getKth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node
        
        dummy = ListNode(next = head)        
        group_prev = dummy
        
        while True:
            kth = getKth(group_prev, k)
            if not kth:
                break
                
            
            group_next = kth.next
            
            prev = kth.next
            curr = group_prev.next
            
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next
            group_prev.next = prev
            
            group_prev = temp
        
        return dummy.next
            
            
            
            
            
        