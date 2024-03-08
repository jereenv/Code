# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node_freq = {}
        
        node = head
        
        while node:
            node_freq[node.val]  = 1 + node_freq.get(node.val,0)
            node = node.next
        
        dummy = ListNode(next = None)
        prev = dummy
        for node in node_freq:
            
            curr = ListNode(val = node_freq[node])
            prev.next = curr
            prev = curr
  
        return dummy.next