# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node_freq = {}
        
        node = None
        
        while head:
            if head.val not in node_freq:
                node_freq[head.val] = ListNode(1, node)
                node = node_freq[head.val]
            else:
                node_freq[head.val].val += 1
            head = head.next
        
        return node